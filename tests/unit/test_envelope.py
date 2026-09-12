"""Tests for raw payload and receipt-envelope semantics."""

import unittest

from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

from kordaxis.ingest import (
    RawEventDraft,
    RawEventEnvelope,
    RawPayload,
)


class RawPayloadTests(unittest.TestCase):
    def test_factory_derives_digest_from_exact_bytes(self) -> None:
        payload = RawPayload.from_bytes(
            content=b'{"event":"login"}',
        )

        self.assertEqual(
            payload.size_bytes,
            17,
        )

        self.assertEqual(
            len(payload.sha256),
            64,
        )

    def test_manual_digest_mismatch_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            RawPayload(
                content=b"evidence",
                sha256="0" * 64,
            )

    def test_payload_is_immutable(self) -> None:
        payload = RawPayload.from_bytes(
            content=b"evidence",
        )

        with self.assertRaises(FrozenInstanceError):
            payload.sha256 = "modified"  # type: ignore[misc]


class RawEventDraftTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = RawPayload.from_bytes(
            content=b'{"event":"repository.read"}',
        )

        self.source_time = datetime(
            2026,
            9,
            12,
            17,
            0,
            tzinfo=UTC,
        )

        self.received_time = datetime(
            2026,
            9,
            12,
            17,
            0,
            1,
            tzinfo=UTC,
        )

    def test_media_type_belongs_to_receipt_not_payload(self) -> None:
        first = RawEventDraft(
            envelope_id="receipt-001",
            source_id="synthetic.git",
            source_event_id="evt-42",
            source_timestamp=self.source_time,
            received_at=self.received_time,
            media_type="application/json",
            payload=self.payload,
        )

        second = RawEventDraft(
            envelope_id="receipt-002",
            source_id="synthetic.git",
            source_event_id="evt-42",
            source_timestamp=self.source_time,
            received_at=self.received_time,
            media_type="application/octet-stream",
            payload=self.payload,
        )

        self.assertEqual(
            first.payload.sha256,
            second.payload.sha256,
        )

        self.assertNotEqual(
            first.media_type,
            second.media_type,
        )

    def test_received_at_must_be_timezone_aware(self) -> None:
        with self.assertRaises(ValueError):
            RawEventDraft(
                envelope_id="receipt-001",
                source_id="synthetic.git",
                source_event_id=None,
                source_timestamp=None,
                received_at=datetime(
                    2026,
                    9,
                    12,
                    17,
                    0,
                ),
                media_type="application/json",
                payload=self.payload,
            )


class RawEventEnvelopeTests(unittest.TestCase):
    def test_database_sequence_materializes_envelope(self) -> None:
        payload = RawPayload.from_bytes(
            content=b"evidence",
        )

        draft = RawEventDraft(
            envelope_id="receipt-001",
            source_id="synthetic.sensor",
            source_event_id=None,
            source_timestamp=None,
            received_at=datetime.now(UTC),
            media_type="application/octet-stream",
            payload=payload,
        )

        envelope = RawEventEnvelope.from_draft(
            draft,
            ingest_sequence=41,
        )

        self.assertEqual(
            envelope.ingest_sequence,
            41,
        )

        self.assertEqual(
            envelope.ordering_key(),
            (
                41,
                "receipt-001",
            ),
        )

    def test_non_positive_ingest_sequence_is_rejected(self) -> None:
        payload = RawPayload.from_bytes(
            content=b"evidence",
        )

        draft = RawEventDraft(
            envelope_id="receipt-001",
            source_id="synthetic.sensor",
            source_event_id=None,
            source_timestamp=None,
            received_at=datetime.now(UTC),
            media_type="application/octet-stream",
            payload=payload,
        )

        with self.assertRaises(ValueError):
            RawEventEnvelope.from_draft(
                draft,
                ingest_sequence=0,
            )


if __name__ == "__main__":
    unittest.main()