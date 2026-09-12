"""Persistence-specific KORDAXIS failures."""


class EvidenceStoreError(RuntimeError):
    """Base class for evidence persistence failures."""


class DuplicateEnvelopeError(EvidenceStoreError):
    """Raised when an envelope identity already exists."""


class EvidenceIntegrityError(EvidenceStoreError):
    """Raised when persisted evidence fails integrity validation."""


class EvidenceCollisionError(EvidenceStoreError):
    """Raised when one digest identifies different exact bytes."""


class EvidenceNotFoundError(EvidenceStoreError):
    """Raised when requested persisted evidence does not exist."""