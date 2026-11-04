import hashlib
from functools import lru_cache
from typing import List, Tuple, Optional


@lru_cache(maxsize=4096)
def fast_double_sha256(data: bytes) -> bytes:
    """Compute double SHA-256 digest with LRU caching for high-frequency payloads."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


class MerkleTreeEngine:
    """High-performance Merkle root generator optimized for block processing."""

    __slots__ = ("_hashes",)

    def __init__(self, raw_txs: List[bytes]):
        self._hashes: List[bytes] = [fast_double_sha256(tx) for tx in raw_txs]

    def get_root(self) -> Optional[bytes]:
        """Compute the Merkle root using iterative fast pair reduction."""
        if not self._hashes:
            return None

        current_nodes = list(self._hashes)
        while len(current_nodes) > 1:
            if len(current_nodes) % 2 == 1:
                current_nodes.append(current_nodes[-1])

            next_level = []
            for i in range(0, len(current_nodes), 2):
                combined = current_nodes[i] + current_nodes[i + 1]
                next_level.append(fast_double_sha256(combined))
            current_nodes = next_level

        return current_nodes[0]

    def verify_tx(self, tx_hash: bytes, merkle_proof: List[Tuple[bool, bytes]], expected_root: bytes) -> bool:
        """Verify transaction inclusion proof against calculated Merkle root."""
        current = tx_hash
        for is_left, sibling_hash in merkle_proof:
            combined = sibling_hash + current if is_left else current + sibling_hash
            current = fast_double_sha256(combined)
        return current == expected_root
