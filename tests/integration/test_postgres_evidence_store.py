"""Integration tests for PostgreSQL raw-evidence persistence."""

import os
import unittest

from datetime import UTC, datetime
from uuid import uuid4

from psycopg import Error as PsycopgError
from psycopg import connect

from kordaxis.ingest import (
    RawEventDraft,
    RawPayload,
)
from kordaxis.persistence import (
    DuplicateEnvelopeError,
    PostgresEvidenceStore,
)


DATABASE_URL = os.getenv(
    "KORDAXIS_TEST_DATABASE_URL"
)


@unittest.skipUnless(
    DATABASE_URL,
    "KORDAXIS_TEST_DATABASE_URL is not configured",
)
class PostgresEvidenceStoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        assert DATABASE_URL is not None

        cls.connection = connect(DATABASE_URL)

        cls.store = PostgresEvidenceStore(
            cls.connection
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.connection.close()

    def _draft(
        self,
        *,
        envelope_id: str | None = None,
        content: bytes | None = None,
        media_type: str = "application/json",
    ) -> RawEventDraft:
        unique = uuid4().hex

        return RawEventDraft(
            envelope_id=(
                envelope_id
                or f"receipt-{unique}"
            ),
            source_id="synthetic.git",
            source_event_id=f"evt-{unique}",
            source_timestamp=datetime.now(UTC),
            received_at=datetime.now(UTC),
            media_type=media_type,
            payload=RawPayload.from_bytes(
                content=(
                    content
                    or f'{{"id":"{unique}"}}'.encode()
                )
            ),
        )

    def test_round_trip_preserves_exact_bytes(self) -> None:
        draft = self._draft(
            content=b'{"exact":"bytes"}',
        )

        persisted = self.store.append(draft)

        loaded = self.store.load(
            persisted.envelope_id
        )

        self.assertEqual(
            loaded.payload.content,
            draft.payload.content,
        )

        self.assertEqual(
            loaded.payload.sha256,
            draft.payload.sha256,
        )

        self.assertEqual(
            loaded.envelope_id,
            draft.envelope_id,
        )

    def test_database_assigns_increasing_ingest_sequence(self) -> None:
        first = self.store.append(
            self._draft()
        )

        second = self.store.append(
            self._draft()
        )

        self.assertGreater(
            second.ingest_sequence,
            first.ingest_sequence,
        )

    def test_same_payload_can_have_multiple_receipts(self) -> None:
        content = b'{"shared":"payload"}'

        first = self.store.append(
            self._draft(
                content=content,
                media_type="application/json",
            )
        )

        second = self.store.append(
            self._draft(
                content=content,
                media_type="application/octet-stream",
            )
        )

        self.assertEqual(
            first.payload.sha256,
            second.payload.sha256,
        )

        self.assertNotEqual(
            first.envelope_id,
            second.envelope_id,
        )

        self.assertNotEqual(
            first.media_type,
            second.media_type,
        )

        with self.connection.transaction():
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT count(*)
                    FROM kordaxis.raw_payloads
                    WHERE sha256 = %s
                    """,
                    (first.payload.sha256,),
                )

                count = cursor.fetchone()[0]

        self.assertEqual(
            count,
            1,
        )

    def test_duplicate_envelope_rolls_back_new_payload(self) -> None:
        envelope_id = f"receipt-{uuid4().hex}"

        first = self._draft(
            envelope_id=envelope_id,
            content=b"first-payload",
        )

        self.store.append(first)

        second = self._draft(
            envelope_id=envelope_id,
            content=b"second-payload",
        )

        with self.assertRaises(DuplicateEnvelopeError):
            self.store.append(second)

        with self.connection.transaction():
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT count(*)
                    FROM kordaxis.raw_payloads
                    WHERE sha256 = %s
                    """,
                    (second.payload.sha256,),
                )

                count = cursor.fetchone()[0]

        self.assertEqual(
            count,
            0,
        )

    def test_raw_envelope_update_is_rejected(self) -> None:
        persisted = self.store.append(
            self._draft()
        )

        with self.assertRaises(PsycopgError):
            with self.connection.transaction():
                with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE kordaxis.raw_event_envelopes
                        SET source_id = 'modified'
                        WHERE envelope_id = %s
                        """,
                        (persisted.envelope_id,),
                    )

    def test_raw_envelope_delete_is_rejected(self) -> None:
        persisted = self.store.append(
            self._draft()
        )

        with self.assertRaises(PsycopgError):
            with self.connection.transaction():
                with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        DELETE FROM kordaxis.raw_event_envelopes
                        WHERE envelope_id = %s
                        """,
                        (persisted.envelope_id,),
                    )

    def test_ordered_loading_uses_ingest_sequence(self) -> None:
        first = self.store.append(
            self._draft()
        )

        second = self.store.append(
            self._draft()
        )

        loaded = self.store.load_after(
            sequence_exclusive=(
                first.ingest_sequence - 1
            ),
            limit=2,
        )

        self.assertEqual(
            [
                item.ingest_sequence
                for item in loaded
            ],
            [
                first.ingest_sequence,
                second.ingest_sequence,
            ],
        )


if __name__ == "__main__":
    unittest.main()