import functools
from typing import Callable, Any, Dict

# Cache for crypto computation results
_CACHE: Dict[tuple, Any] = {}

def memoize_crypto(func: Callable) -> Callable:
    """Decorator for caching intensive crypto calculations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

class CryptoProcessor:
    """Core processor with performance-focused operations."""
    
    def __init__(self, buffer_size: int = 1024):
        self.buffer_size = buffer_size

    @memoize_crypto
    def compute_hash_sequence(self, data: bytes, iterations: int) -> bytes:
        """Performance-optimized iterative hashing."""
        import hashlib
        result = data
        for _ in range(iterations):
            result = hashlib.sha256(result).digest()
        return result

    def batch_process(self, items: list) -> list:
        """Map processing over items using cached results."""
        return [self.compute_hash_sequence(item, 1000) for item in items]

# Global processor instance for module access
processor = CryptoProcessor()