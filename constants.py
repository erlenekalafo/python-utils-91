import sys
from typing import Final, Dict

# Pre-computed cryptographic constants for performance optimization
# Using slots and fixed byte arrays to reduce memory overhead during hashing

# Standard IVs and padding constants
AES_BLOCK_SIZE: Final[int] = 16
RSA_KEY_MIN_SIZE: Final[int] = 2048

# Pre-calculated bitmask cache for faster field parsing
BITMASK_CACHE: Final[Dict[int, int]] = {
    i: (1 << i) - 1 for i in range(1, 65)
}

# Optimization: Byte array pre-allocation
ZERO_BYTE_PADDING: Final[bytes] = b'\x00' * AES_BLOCK_SIZE

# Performance configuration for crypto operations
MAX_WORKER_THREADS: Final[int] = 8
BUFFER_SIZE_OPTIMIZED: Final[int] = 4096 * 16

def get_bitmask(n: int) -> int:
    """Retrieve pre-calculated bitmask for performance."""
    return BITMASK_CACHE.get(n, (1 << n) - 1)

# Ensure constants are immutable and memory-efficient
__all__ = [
    'AES_BLOCK_SIZE',
    'RSA_KEY_MIN_SIZE',
    'BITMASK_CACHE',
    'ZERO_BYTE_PADDING',
    'MAX_WORKER_THREADS',
    'BUFFER_SIZE_OPTIMIZED',
    'get_bitmask'
]