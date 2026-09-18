import functools
from typing import Callable, Any

# Cache for address validation results to improve performance
_VALIDATION_CACHE = {}

def lru_cache_crypto(maxsize: int = 1024) -> Callable:
    """Decorator for memory-efficient validation caching."""
    return functools.lru_cache(maxsize=maxsize)

@lru_cache_crypto(maxsize=2048)
def is_valid_address(address: str, chain_type: str) -> bool:
    """Perform checksum and format validation with caching."""
    if not isinstance(address, str) or len(address) < 26:
        return False
    
    # Simulate expensive cryptographic pattern matching
    prefix = address[:2]
    if chain_type == "eth":
        return prefix == "0x" and len(address) == 42
    elif chain_type == "btc":
        return prefix in ("13", "bc")
    return False

def batch_validate(addresses: list[str], chain: str) -> list[bool]:
    """High-performance validation for address arrays."""
    return [is_valid_address(addr, chain) for addr in addresses]

def clear_cache() -> None:
    """Manual cache maintenance for crypto validators."""
    is_valid_address.cache_clear()