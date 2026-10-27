import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class CryptoUtils:
    @staticmethod
    def validate_key_length(key: bytes, expected_length: int) -> bool:
        """Verify cryptographic key matches required byte length."""
        if not isinstance(key, (bytes, bytearray)):
            logger.error("Invalid key type provided")
            return False
        return len(key) == expected_length

    @staticmethod
    def safe_hex_to_bytes(hex_str: str) -> Optional[bytes]:
        """Convert hex string to bytes with recovery logic."""
        try:
            if not hex_str:
                return None
            return bytes.fromhex(hex_str)
        except (ValueError, TypeError) as e:
            logger.warning(f"Malformed hex string: {e}")
            return None

    @staticmethod
    def secure_truncate(data: bytes, limit: int) -> bytes:
        """Truncate data safely without index errors."""
        if limit < 0:
            return b''
        return data[:limit]

    @staticmethod
    def checksum_verify(data: bytes, expected: bytes) -> bool:
        """Constant-time comparison for cryptographic integrity."""
        if len(data) != len(expected):
            return False
        
        result = 0
        for x, y in zip(data, expected):
            result |= x ^ y
        return result == 0