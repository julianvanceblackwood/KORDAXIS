"""Tests for immutable raw payload and receipt-envelope semantics."""

import unittest
from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

from kordaxis.ingest import RawEventEnvelope, RawPayload


class RawPayloadTests(unittest.TestCase):
    def test_factory_derives_digest_from_exact_bytes(self) -> None:
        payload = RawPayload.from_bytes(
            content=b'{"event":"login"}',
            media_type="application/json",
        )

        self.assertEqual(payload.size_bytes, 17)
        self.assertEqual(len(payload.sha256), 64)

    def test_manual_digest_mismatch_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            RawPayload(
                content=b"evidence",
                sha256="0" * 64,
                media_type="application/octet-stream",
            )

    def test_payload_is_immutable(self) -> None:
        payload = RawPayload.from_bytes(
            content=b"evidence",
            media_type="application/octet-stream",
        )

        with self.assertRaises(FrozenInstanceError):
            payload.media_type = "text/plain"  # type: ignore[misc]


class RawEventEnvelopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = RawPayload.from_bytes(
            content=b'{"event":"repository.read"}',
            media_type="application/json",
        )
        self.source_time = datetime(2026, 9, 12, 17, 0, tzinfo=UTC)
        self.received_time = datetime(2026, 9, 12, 17, 0, 1, tzinfo=UTC)

    def _envelope(self, *, envelope_id: str, sequence: int) -> RawEventEnvelope:
        return RawEventEnvelope(
            envelope_id=envelope_id,
            source_id="synthetic.git",
            source_event_id="evt-42",
            source_timestamp=self.source_time,
            received_at=self.received_time,
            ingest_sequence=sequence,
            payload=self.payload,
        )

    def test_duplicate_deliveries_remain_distinct_receipt_episodes(self) -> None:
        first = self._envelope(envelope_id="receipt-001", sequence=10)
        duplicate = self._envelope(envelope_id="receipt-002", sequence=11)

        self.assertEqual(first.source_event_id, duplicate.source_event_id)
        self.assertEqual(first.payload.sha256, duplicate.payload.sha256)
        self.assertNotEqual(first.envelope_id, duplicate.envelope_id)
        self.assertNotEqual(first.ingest_sequence, duplicate.ingest_sequence)
        self.assertNotEqual(first, duplicate)

    def test_equal_source_timestamps_still_have_deterministic_receipt_order(self) -> None:
        later_receipt = self._envelope(envelope_id="receipt-b", sequence=22)
        earlier_receipt = self._envelope(envelope_id="receipt-a", sequence=21)

        ordered = sorted(
            [later_receipt, earlier_receipt],
            key=RawEventEnvelope.ordering_key,
        )

        self.assertEqual(
            [item.envelope_id for item in ordered],
            ["receipt-a", "receipt-b"],
        )

    def test_received_at_must_be_timezone_aware(self) -> None:
        with self.assertRaises(ValueError):
            RawEventEnvelope(
                envelope_id="receipt-001",
                source_id="synthetic.git",
                source_event_id="evt-42",
                source_timestamp=self.source_time,
                received_at=datetime(2026, 9, 12, 17, 0, 1),
                ingest_sequence=1,
                payload=self.payload,
            )

    def test_source_timestamp_must_be_timezone_aware_when_present(self) -> None:
        with self.assertRaises(ValueError):
            RawEventEnvelope(
                envelope_id="receipt-001",
                source_id="synthetic.git",
                source_event_id="evt-42",
                source_timestamp=datetime(2026, 9, 12, 17, 0),
                received_at=self.received_time,
                ingest_sequence=1,
                payload=self.payload,
            )

    def test_negative_ingest_sequence_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self._envelope(envelope_id="receipt-001", sequence=-1)

    def test_envelope_is_immutable(self) -> None:
        envelope = self._envelope(envelope_id="receipt-001", sequence=1)

        with self.assertRaises(FrozenInstanceError):
            envelope.source_id = "modified"  # type: ignore[misc]


if __name__ == "__main__":
    unittest.main()
