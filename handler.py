import functools
from typing import Dict, Any

# Cache for crypto hash computations to avoid redundant processing
_HASH_CACHE: Dict[bytes, bytes] = {}
MAX_CACHE_SIZE = 1000

def memoize_crypto_hash(func):
    """Decorator to cache crypto operation results."""
    @functools.wraps(func)
    def wrapper(data: bytes, *args, **kwargs):
        if data in _HASH_CACHE:
            return _HASH_CACHE[data]
        
        result = func(data, *args, **kwargs)
        
        if len(_HASH_CACHE) >= MAX_CACHE_SIZE:
            _HASH_CACHE.clear()
            
        _HASH_CACHE[data] = result
        return result
    return wrapper

@memoize_crypto_hash
def compute_sha256_digest(data: bytes) -> bytes:
    """Performance optimized SHA256 hashing for bulk processing."""
    import hashlib
    return hashlib.sha256(data).digest()

class CryptoHandler:
    """Handles high-frequency crypto processing tasks."""
    
    def process_batch(self, payloads: list[bytes]) -> list[bytes]:
        """Process batches with memoized overhead reduction."""
        return [compute_sha256_digest(p) for p in payloads]