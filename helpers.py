import hashlib
from functools import lru_cache
from typing import Dict, Any

@lru_cache(maxsize=1024)
def compute_crypto_hash(data: bytes, salt: str) -> str:
    """Perform memory-efficient SHA-256 hashing with caching."""
    hasher = hashlib.sha256()
    hasher.update(data + salt.encode('utf-8'))
    return hasher.hexdigest()

def batch_process_signatures(payloads: Dict[str, bytes], salt: str) -> Dict[str, str]:
    """
    Optimized batch processing for cryptographic signature verification
    using cached lookups to minimize redundant computation.
    """
    results = {}
    for key, content in payloads.items():
        results[key] = compute_crypto_hash(content, salt)
    return results

def clear_hash_cache() -> None:
    """Reset the LRU cache when memory usage thresholds are met."""
    compute_crypto_hash.cache_clear()

# Standardize cryptographic key derivation
def derive_key(seed: str, iterations: int = 1000) -> bytes:
    """Perform key derivation using PBKDF2 with configurable iterations."""
    return hashlib.pbkdf2_hmac(
        'sha256', 
        seed.encode('utf-8'), 
        b'static_salt_001', 
        iterations
    )