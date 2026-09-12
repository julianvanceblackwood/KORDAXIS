"""Immutable raw-ingress domain objects."""

from dataclasses import dataclass
from datetime import datetime
from typing import Self

from .digest import sha256_bytes


def _require_non_empty(name: str, value: str) -> None:
    if not value.strip():
        raise ValueError(f"{name} must not be empty")


def _require_aware_datetime(name: str, value: datetime) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{name} must be timezone-aware")


@dataclass(frozen=True, slots=True)
class RawPayload:
    """Exact immutable payload bytes and their integrity metadata."""

    content: bytes
    sha256: str
    media_type: str

    def __post_init__(self) -> None:
        if not isinstance(self.content, bytes):
            raise TypeError("content must be exact immutable bytes")

        _require_non_empty("media_type", self.media_type)

        expected_digest = sha256_bytes(self.content)
        if self.sha256 != expected_digest:
            raise ValueError("sha256 does not match the exact payload bytes")

    @classmethod
    def from_bytes(cls, *, content: bytes, media_type: str) -> Self:
        """Create a payload while deriving its digest from the exact input bytes."""

        return cls(
            content=content,
            sha256=sha256_bytes(content),
            media_type=media_type,
        )

    @property
    def size_bytes(self) -> int:
        """Return the exact payload size without storing redundant mutable state."""

        return len(self.content)


@dataclass(frozen=True, slots=True)
class RawEventEnvelope:
    """One immutable receipt episode at the KORDAXIS ingestion boundary.

    Two deliveries of the same upstream event remain two envelopes. They may share
    the same payload digest and source event identifier while retaining distinct
    envelope identifiers and ingest sequence numbers.
    """

    envelope_id: str
    source_id: str
    source_event_id: str | None
    source_timestamp: datetime | None
    received_at: datetime
    ingest_sequence: int
    payload: RawPayload
    ingest_contract_version: str = "raw-event-envelope/v1"

    def __post_init__(self) -> None:
        _require_non_empty("envelope_id", self.envelope_id)
        _require_non_empty("source_id", self.source_id)
        _require_non_empty("ingest_contract_version", self.ingest_contract_version)

        if self.source_event_id is not None:
            _require_non_empty("source_event_id", self.source_event_id)

        _require_aware_datetime("received_at", self.received_at)

        if self.source_timestamp is not None:
            _require_aware_datetime("source_timestamp", self.source_timestamp)

        if self.ingest_sequence < 0:
            raise ValueError("ingest_sequence must be non-negative")

    def ordering_key(self) -> tuple[int, str]:
        """Return the Generation-0 deterministic receipt-order key.

        Generation 0 has one authoritative ingest sequence. ``envelope_id`` is a
        deterministic tie-breaker for defensive programming; production code should
        treat duplicate sequence assignment as an ingestion defect rather than rely
        on the tie-breaker.
        """

        return (self.ingest_sequence, self.envelope_id)
