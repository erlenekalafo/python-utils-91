import hashlib
from functools import lru_cache
from typing import List, Union


@lru_cache(maxsize=1024)
def fast_sha256(data: bytes) -> str:
    """Compute and cache SHA-256 hash for binary data."""
    return hashlib.sha256(data).hexdigest()


def batch_hash_verification(
    data_blocks: List[bytes], expected_hashes: List[str]
) -> List[bool]:
    """Verify a batch of data blocks against expected hashes efficiently.
    
    Uses cached hash function to speed up repeated lookups.
    """
    if len(data_blocks) != len(expected_hashes):
        raise ValueError("Block count must match hash count")

    results = []
    for block, expected in zip(data_blocks, expected_hashes):
        calculated = fast_sha256(block)
        results.append(calculated.lower() == expected.lower())

    return results


class NonceSearcher:
    """Optimized proof-of-work nonce search utility."""

    def __init__(self, prefix_zeros: int = 4):
        self.target_prefix = "0" * prefix_zeros

    def find_nonce(self, base_data: bytes, max_iterations: int = 1000000) -> Union[int, None]:
        """Find a nonce that produces a hash starting with target zeros."""
        target = self.target_prefix
        sha = hashlib.sha256

        for nonce in range(max_iterations):
            candidate = base_data + nonce.to_bytes(8, byteorder="big")
            digest = sha(candidate).hexdigest()
            if digest.startswith(target):
                return nonce
        return None
