import hashlib
from typing import Sequence

class CryptoHasher:
    """Provides optimized cryptographic hashing helpers for blockchain data structures."""
    
    def __init__(self):
        # Cache the empty hasher to bypass initialization overhead during copy operations
        self._base_sha256 = hashlib.sha256()

    def double_sha256(self, data: bytes) -> bytes:
        """Compute double SHA-256 hash using hasher cloning for high throughput."""
        h1 = self._base_sha256.copy()
        h1.update(data)
        h2 = self._base_sha256.copy()
        h2.update(h1.digest())
        return h2.digest()

    def compute_merkle_root(self, leaves: Sequence[bytes]) -> bytes:
        """
        Compute the Merkle root from a sequence of transaction hashes.
        Optimized to reduce memory overhead and speed up execution.
        """
        if not leaves:
            return b""
        
        # Local reference lookup optimization to speed up loop execution
        d_sha256 = self.double_sha256
        tree_level = list(leaves)
        length = len(tree_level)
        
        while length > 1:
            tree_level = [
                d_sha256(tree_level[i] + (tree_level[i + 1] if i + 1 < length else tree_level[i]))
                for i in range(0, length, 2)
            ]
            length = len(tree_level)
            
        return tree_level[0]
