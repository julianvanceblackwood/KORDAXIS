"""PostgreSQL persistence for append-only raw evidence."""

from collections.abc import Sequence

from psycopg import Connection
from psycopg.errors import UniqueViolation

from kordaxis.ingest import (
    RawEventDraft,
    RawEventEnvelope,
    RawPayload,
)

from .errors import (
    DuplicateEnvelopeError,
    EvidenceCollisionError,
    EvidenceIntegrityError,
    EvidenceNotFoundError,
)


class PostgresEvidenceStore:
    """Persist and recover raw evidence using PostgreSQL."""

    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    def append(
        self,
        draft: RawEventDraft,
    ) -> RawEventEnvelope:
        """Atomically persist payload content and one receipt episode."""

        try:
            with self._connection.transaction():
                with self._connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO kordaxis.raw_payloads (
                            sha256,
                            content
                        )
                        VALUES (%s, %s)
                        ON CONFLICT (sha256) DO NOTHING
                        """,
                        (
                            draft.payload.sha256,
                            draft.payload.content,
                        ),
                    )

                    cursor.execute(
                        """
                        SELECT content
                        FROM kordaxis.raw_payloads
                        WHERE sha256 = %s
                        """,
                        (draft.payload.sha256,),
                    )

                    payload_row = cursor.fetchone()

                    if payload_row is None:
                        raise EvidenceIntegrityError(
                            "payload disappeared during persistence"
                        )

                    stored_content = bytes(payload_row[0])

                    if stored_content != draft.payload.content:
                        raise EvidenceCollisionError(
                            "one SHA-256 digest resolved to "
                            "different exact payload bytes"
                        )

                    cursor.execute(
                        """
                        INSERT INTO kordaxis.raw_event_envelopes (
                            envelope_id,
                            source_id,
                            source_event_id,
                            source_timestamp,
                            received_at,
                            media_type,
                            payload_sha256,
                            ingest_contract_version
                        )
                        VALUES (
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                        )
                        RETURNING ingest_sequence
                        """,
                        (
                            draft.envelope_id,
                            draft.source_id,
                            draft.source_event_id,
                            draft.source_timestamp,
                            draft.received_at,
                            draft.media_type,
                            draft.payload.sha256,
                            draft.ingest_contract_version,
                        ),
                    )

                    sequence_row = cursor.fetchone()

                    if sequence_row is None:
                        raise EvidenceIntegrityError(
                            "database did not return ingest sequence"
                        )

                    ingest_sequence = int(sequence_row[0])

        except UniqueViolation as exc:
            if (
                exc.diag.constraint_name
                == "raw_event_envelopes_pkey"
            ):
                raise DuplicateEnvelopeError(
                    f"envelope already exists: "
                    f"{draft.envelope_id}"
                ) from exc

            raise

        return RawEventEnvelope.from_draft(
            draft,
            ingest_sequence=ingest_sequence,
        )

    def load(
        self,
        envelope_id: str,
    ) -> RawEventEnvelope:
        """Load one envelope and revalidate exact payload integrity."""

        with self._connection.transaction():
            with self._connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        e.envelope_id,
                        e.source_id,
                        e.source_event_id,
                        e.source_timestamp,
                        e.received_at,
                        e.media_type,
                        e.ingest_sequence,
                        e.ingest_contract_version,
                        p.sha256,
                        p.content
                    FROM kordaxis.raw_event_envelopes AS e
                    JOIN kordaxis.raw_payloads AS p
                      ON p.sha256 = e.payload_sha256
                    WHERE e.envelope_id = %s
                    """,
                    (envelope_id,),
                )

                row = cursor.fetchone()

        if row is None:
            raise EvidenceNotFoundError(
                f"envelope not found: {envelope_id}"
            )

        return self._row_to_envelope(row)

    def load_after(
        self,
        *,
        sequence_exclusive: int,
        limit: int = 1000,
    ) -> Sequence[RawEventEnvelope]:
        """Load receipt episodes in authoritative ingest order."""

        if sequence_exclusive < 0:
            raise ValueError(
                "sequence_exclusive must be non-negative"
            )

        if not 1 <= limit <= 10_000:
            raise ValueError(
                "limit must be between 1 and 10000"
            )

        with self._connection.transaction():
            with self._connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        e.envelope_id,
                        e.source_id,
                        e.source_event_id,
                        e.source_timestamp,
                        e.received_at,
                        e.media_type,
                        e.ingest_sequence,
                        e.ingest_contract_version,
                        p.sha256,
                        p.content
                    FROM kordaxis.raw_event_envelopes AS e
                    JOIN kordaxis.raw_payloads AS p
                      ON p.sha256 = e.payload_sha256
                    WHERE e.ingest_sequence > %s
                    ORDER BY e.ingest_sequence ASC
                    LIMIT %s
                    """,
                    (
                        sequence_exclusive,
                        limit,
                    ),
                )

                rows = cursor.fetchall()

        return [
            self._row_to_envelope(row)
            for row in rows
        ]

    @staticmethod
    def _row_to_envelope(
        row: tuple[object, ...],
    ) -> RawEventEnvelope:
        """Convert one database row into a validated domain object."""

        try:
            payload = RawPayload(
                sha256=str(row[8]),
                content=bytes(row[9]),
            )

            return RawEventEnvelope(
                envelope_id=str(row[0]),
                source_id=str(row[1]),
                source_event_id=(
                    None
                    if row[2] is None
                    else str(row[2])
                ),
                source_timestamp=row[3],  # type: ignore[arg-type]
                received_at=row[4],  # type: ignore[arg-type]
                media_type=str(row[5]),
                ingest_sequence=int(row[6]),
                ingest_contract_version=str(row[7]),
                payload=payload,
            )

        except (TypeError, ValueError) as exc:
            raise EvidenceIntegrityError(
                "persisted raw evidence failed "
                "domain integrity validation"
            ) from exc