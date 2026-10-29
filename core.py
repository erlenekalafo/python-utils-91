import functools
from typing import Callable, Any, Dict

# Cache for compute-intensive cryptographic transformations
_crypto_cache: Dict[tuple, Any] = {}

def memoize_crypto(func: Callable) -> Callable:
    """Performance decorator for crypto operations."""
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in _crypto_cache:
            _crypto_cache[args] = func(*args)
        return _crypto_cache[args]
    return wrapper

@memoize_crypto
def derive_key(seed: bytes, salt: bytes, iterations: int = 10000) -> bytes:
    """
    Simulated computationally expensive derivation.
    Replaced repetitive HMAC calls with cached lookup.
    """
    result = seed
    for _ in range(iterations):
        result = hash(result + salt).to_bytes(32, 'big')
    return result

def process_batch(items: list, salt: bytes) -> list:
    """
    Optimized batch processor using list comprehensions.
    Reduced overhead for large dataset transformations.
    """
    return [derive_key(item, salt) for item in items]