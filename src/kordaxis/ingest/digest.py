"""SHA-256 helpers for preserved byte content."""

from hashlib import sha256


def sha256_bytes(payload: bytes) -> str:
    """Return the SHA-256 hex digest of the supplied byte sequence.

    The function accepts only ``bytes`` so callers cannot accidentally hash
    decoded, parsed, or normalized representations. It establishes content
    identity only; callers remain responsible for supplying the preserved
    ingress bytes.
    """

    if not isinstance(payload, bytes):
        raise TypeError("payload must be exact immutable bytes")

    return sha256(payload).hexdigest()
