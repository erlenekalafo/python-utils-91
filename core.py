import functools
import hashlib
import time
from typing import Callable, Any, Dict

# Cache for compute-heavy cryptographic hashing operations
_HASH_CACHE: Dict[tuple, bytes] = {}

def memoize_hash(func: Callable) -> Callable:
    """Decorator to cache expensive hash function results."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> bytes:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in _HASH_CACHE:
            _HASH_CACHE[key] = func(*args, **kwargs)
        return _HASH_CACHE[key]
    return wrapper

@memoize_hash
def compute_sha256(data: bytes) -> bytes:
    """Performance-optimized SHA-256 calculation with caching."""
    return hashlib.sha256(data).digest()

class CryptoProcessor:
    """Core processor for crypto utility operations."""
    def __init__(self, limit: int = 1000):
        self.limit = limit

    def batch_process(self, datasets: list[bytes]) -> list[bytes]:
        """Process batches with memoization to reduce CPU load."""
        results = []
        for data in datasets:
            results.append(compute_sha256(data))
        return results

def clear_cache() -> None:
    """Manual cache clearance to prevent memory leakage."""
    _HASH_CACHE.clear()