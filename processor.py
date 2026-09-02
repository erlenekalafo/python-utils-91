import hashlib
from typing import Any, Dict, List
class CryptoProcessor:
    """A utility class for processing cryptographic data and simple blockchain operations."""
    def __init__(self, secret: str) -> None:
        """Initialize with a secret key for hashing.

        Args:
            secret: Secret string used as key in all hashes.
        """
        self.secret = secret.encode('utf-8')
    def _hash(self, data: bytes) -> str:
        """Compute SHA256 hash prefixed with secret.

        Args:
            data: Input bytes to be hashed.
        Returns:
            Hexadecimal string of the hash.
        """
        # Combine secret and data for keyed hash
        hasher = hashlib.sha256(self.secret + data)
        return hasher.hexdigest()
    def hash_data(self, data: str) -> str:
        """Hash string data.

        Args:
            data: String to hash.
        Returns:
            Hash as hex string.
        """
        return self._hash(data.encode('utf-8'))
    def process_transaction(self, tx: Dict[str, Any]) -> Dict[str, Any]:
        """Process a transaction by adding its hash.

        Args:
            tx: Transaction dictionary with fields like 'from', 'to', 'amount'.
        Returns:
            The transaction with added 'tx_hash' field.
        """
        # Serialize for consistent hashing
        items = sorted(tx.items())
        serialized = str(items).encode('utf-8')
        tx_hash = self._hash(serialized)
        result = tx.copy()
        result['tx_hash'] = tx_hash
        return result
    def create_block(self, data: Dict[str, Any], prev_hash: str = "") -> Dict[str, Any]:
        """Create a new block with data and previous hash.

        Args:
            data: The block data dictionary.
            prev_hash: Hash of the previous block, empty for genesis.
        Returns:
            Block dictionary with 'data', 'prev_hash', 'hash'.
        """
        serialized_data = str(sorted(data.items())).encode('utf-8')
        # Hash includes prev_hash for chain linking
        to_hash = serialized_data + prev_hash.encode('utf-8')
        block_hash = self._hash(to_hash)
        return {'data': data, 'prev_hash': prev_hash, 'hash': block_hash}
    def validate_chain(self, chain: List[Dict[str, Any]]) -> bool:
        """Validate the blockchain integrity.

        Checks each block's hash and previous hash links.

        Args:
            chain: List of block dictionaries.
        Returns:
            True if valid, else False.
        """
        if len(chain) == 0:
            return True
        if chain[0]['prev_hash'] != "":
            return False
        for i in range(len(chain)):
            block = chain[i]
            data = block['data']
            prev = block['prev_hash']
            expected_hash = block['hash']
            serialized_data = str(sorted(data.items())).encode('utf-8')
            to_hash = serialized_data + prev.encode('utf-8')
            computed = self._hash(to_hash)
            if computed != expected_hash:
                return False
            if i > 0 and prev != chain[i-1]['hash']:
                return False
        return True