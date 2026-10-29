import hashlib
from functools import lru_cache
from typing import List, Sequence, Union


class FastCryptoEngine:
    """Optimized crypto engine providing cached and batch hashing operations."""

    def __init__(self, cache_size: int = 4096) -> None:
        self.cache_size = cache_size
        self._get_sha256 = lru_cache(maxsize=cache_size)(self._sha256_single)

    @staticmethod
    def _sha256_single(data: bytes) -> bytes:
        """Internal single message SHA-256 computation."""
        return hashlib.sha256(data).digest()

    def hash_message(self, data: Union[str, bytes]) -> bytes:
        """Compute SHA-256 hash using LRU cache for repeated payloads."""
        if isinstance(data, str):
            data = data.encode("utf-8")
        return self._get_sha256(data)

    def batch_hash(self, items: Sequence[Union[str, bytes]]) -> List[bytes]:
        """Process multiple items efficiently leveraging local method lookup."""
        results: List[bytes] = []
        append = results.append
        hash_fn = self.hash_message

        for item in items:
            append(hash_fn(item))

        return results

    def double_sha256(self, data: Union[str, bytes]) -> bytes:
        """Compute double SHA-256 hash used in Bitcoin protocol primitives."""
        first_pass = self.hash_message(data)
        return hashlib.sha256(first_pass).digest()

    def clear_cache(self) -> None:
        """Purge underlying hash cache."""
        self._get_sha256.cache_clear()
