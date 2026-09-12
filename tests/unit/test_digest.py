"""Tests for exact-byte SHA-256 semantics."""

import unittest

from kordaxis.ingest import sha256_bytes


class Sha256BytesTests(unittest.TestCase):
    def test_same_exact_bytes_produce_same_digest(self) -> None:
        payload = b'{"event":"login"}'

        self.assertEqual(sha256_bytes(payload), sha256_bytes(payload))

    def test_byte_level_difference_changes_digest(self) -> None:
        compact = b'{"event":"login"}'
        spaced = b'{"event": "login"}'

        self.assertNotEqual(sha256_bytes(compact), sha256_bytes(spaced))

    def test_mutable_bytearray_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            sha256_bytes(bytearray(b"mutable"))  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
