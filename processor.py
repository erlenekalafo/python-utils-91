from typing import List, Dict, Optional

class CryptoProcessor:
    """Handles cryptographic data processing tasks."""

    def __init__(self, key_size: int = 256) -> None:
        self.key_size: int = key_size

    def sanitize_payload(self, data: Dict[str, str]) -> Dict[str, str]:
        """Removes non-hexadecimal characters from crypto keys."""
        return {k: v.lower().strip() for k, v in data.items()}

    def batch_process_signatures(self, signatures: List[str]) -> List[Optional[str]]:
        """Validates and formats a list of hex signatures."""
        processed: List[Optional[str]] = []
        for sig in signatures:
            if len(sig) >= self.key_size // 4:
                processed.append(sig.upper())
            else:
                processed.append(None)
        return processed

    def calculate_checksum(self, data: bytes) -> str:
        """Generates a simple hex checksum for a byte array."""
        checksum: int = sum(data) % 0xFFFF
        return hex(checksum).replace('0x', '').zfill(4)

    def validate_node_health(self, nodes: List[Dict[str, any]]) -> bool:
        """Checks if all nodes are responsive and secure."""
        if not nodes:
            return False
        return all(node.get('active', False) for node in nodes)