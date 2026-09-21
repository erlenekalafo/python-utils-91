from hashlib import sha256
from functools import lru_cache
from typing import List, Optional, Dict


@lru_cache(maxsize=4096)
def _double_sha256(data: bytes) -> bytes:
    """Compute cached double SHA-256 hash for repeated transaction nodes."""
    return sha256(sha256(data).digest()).digest()


class FastMerkleTree:
    """Optimized Merkle tree generator for high-throughput crypto transaction batches."""

    def __init__(self, leaf_hashes: Optional[List[bytes]] = None):
        self._leaves: List[bytes] = leaf_hashes if leaf_hashes else []

    def add_leaf(self, tx_hash: bytes) -> None:
        """Add a 32-byte raw transaction hash to the tree leaves."""
        if len(tx_hash) != 32:
            raise ValueError("Transaction hash must be 32 bytes")
        self._leaves.append(tx_hash)

    def compute_root(self) -> bytes:
        """Compute the Merkle root efficiently using cached pairwise hashing."""
        if not self._leaves:
            return b"\x00" * 32

        current_level = list(self._leaves)

        while len(current_level) > 1:
            if len(current_level) % 2 != 0:
                current_level.append(current_level[-1])

            next_level = []
            for i in range(0, len(current_level), 2):
                combined = current_level[i] + current_level[i + 1]
                next_level.append(_double_sha256(combined))

            current_level = next_level

        return current_level[0]

    def batch_verify_membership(self, target_hashes: List[bytes]) -> Dict[bytes, bool]:
        """Perform optimized set-based lookup for batch transaction membership."""
        leaf_set = set(self._leaves)
        return {target: target in leaf_set for target in target_hashes}
