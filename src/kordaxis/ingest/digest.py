"""Cryptographic digests for exact ingress bytes."""

from hashlib import sha256


def sha256_bytes(payload: bytes) -> str:
    """Return the SHA-256 hex digest of the exact bytes received at ingress.

    The function intentionally accepts only ``bytes``. Mutable or already-parsed
    representations are rejected so callers cannot accidentally hash a normalized
    form instead of the evidence that actually arrived.
    """

    if not isinstance(payload, bytes):
        raise TypeError("payload must be exact immutable bytes")

    return sha256(payload).hexdigest()
