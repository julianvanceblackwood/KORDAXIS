"""Immutable raw-ingress domain objects."""

from dataclasses import dataclass
from datetime import datetime
from typing import Self

from .digest import sha256_bytes


def _require_non_empty(name: str, value: str) -> None:
    """Reject empty or whitespace-only textual identifiers."""

    if not value.strip():
        raise ValueError(f"{name} must not be empty")


def _require_aware_datetime(name: str, value: datetime) -> None:
    """Require a datetime with an explicit UTC offset."""

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{name} must be timezone-aware")


@dataclass(frozen=True, slots=True)
class RawPayload:
    """Exact immutable payload bytes and their content identity."""

    content: bytes
    sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.content, bytes):
            raise TypeError("content must be exact immutable bytes")

        expected_digest = sha256_bytes(self.content)

        if self.sha256 != expected_digest:
            raise ValueError(
                "sha256 does not match the exact payload bytes"
            )

    @classmethod
    def from_bytes(cls, *, content: bytes) -> Self:
        """Create a payload and derive identity from the exact bytes."""

        return cls(
            content=content,
            sha256=sha256_bytes(content),
        )

    @property
    def size_bytes(self) -> int:
        """Return the exact payload length."""

        return len(self.content)


@dataclass(frozen=True, slots=True)
class RawEventDraft:
    """A receipt episode before persistence assigns ingest order."""

    envelope_id: str
    source_id: str
    source_event_id: str | None
    source_timestamp: datetime | None
    received_at: datetime
    media_type: str
    payload: RawPayload
    ingest_contract_version: str = "raw-event-envelope/v1"

    def __post_init__(self) -> None:
        _require_non_empty("envelope_id", self.envelope_id)
        _require_non_empty("source_id", self.source_id)
        _require_non_empty("media_type", self.media_type)
        _require_non_empty(
            "ingest_contract_version",
            self.ingest_contract_version,
        )

        if self.source_event_id is not None:
            _require_non_empty(
                "source_event_id",
                self.source_event_id,
            )

        _require_aware_datetime(
            "received_at",
            self.received_at,
        )

        if self.source_timestamp is not None:
            _require_aware_datetime(
                "source_timestamp",
                self.source_timestamp,
            )


@dataclass(frozen=True, slots=True)
class RawEventEnvelope:
    """A persisted immutable KORDAXIS receipt episode."""

    envelope_id: str
    source_id: str
    source_event_id: str | None
    source_timestamp: datetime | None
    received_at: datetime
    media_type: str
    ingest_sequence: int
    payload: RawPayload
    ingest_contract_version: str = "raw-event-envelope/v1"

    def __post_init__(self) -> None:
        _require_non_empty("envelope_id", self.envelope_id)
        _require_non_empty("source_id", self.source_id)
        _require_non_empty("media_type", self.media_type)
        _require_non_empty(
            "ingest_contract_version",
            self.ingest_contract_version,
        )

        if self.source_event_id is not None:
            _require_non_empty(
                "source_event_id",
                self.source_event_id,
            )

        _require_aware_datetime(
            "received_at",
            self.received_at,
        )

        if self.source_timestamp is not None:
            _require_aware_datetime(
                "source_timestamp",
                self.source_timestamp,
            )

        if self.ingest_sequence <= 0:
            raise ValueError(
                "ingest_sequence must be positive"
            )

    @classmethod
    def from_draft(
        cls,
        draft: RawEventDraft,
        *,
        ingest_sequence: int,
    ) -> Self:
        """Materialize a persisted envelope from a receipt draft."""

        return cls(
            envelope_id=draft.envelope_id,
            source_id=draft.source_id,
            source_event_id=draft.source_event_id,
            source_timestamp=draft.source_timestamp,
            received_at=draft.received_at,
            media_type=draft.media_type,
            ingest_sequence=ingest_sequence,
            payload=draft.payload,
            ingest_contract_version=draft.ingest_contract_version,
        )

    def ordering_key(self) -> tuple[int, str]:
        """Return the deterministic receipt-order key."""

        return (
            self.ingest_sequence,
            self.envelope_id,
        )