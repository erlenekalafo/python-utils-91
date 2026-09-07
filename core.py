import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class CryptoProcessor:
    """Handles core cryptographic operations with input validation."""

    def __init__(self, key: str):
        if not key or len(key) < 32:
            raise ValueError("Key must be at least 32 characters.")
        self._key = key.encode()

    def encrypt_data(self, data: Any) -> Optional[bytes]:
        """Encrypts provided data with safe error handling."""
        try:
            if not isinstance(data, str):
                raise TypeError("Input data must be a string")
            
            # Simulate processing logic
            payload = data.encode('utf-8')
            return bytes([b ^ self._key[i % len(self._key)] for i, b in enumerate(payload)])
            
        except TypeError as e:
            logger.error(f"Type mismatch in encryption: {e}")
        except Exception as e:
            logger.critical(f"Unexpected crypto failure: {e}")
            
        return None

    def decrypt_data(self, encrypted: Optional[bytes]) -> str:
        """Decrypts data, returning empty string on failure."""
        if encrypted is None:
            return ""
            
        try:
            decrypted = [b ^ self._key[i % len(self._key)] for i, b in enumerate(encrypted)]
            return bytes(decrypted).decode('utf-8')
        except (UnicodeDecodeError, IndexError) as e:
            logger.warning(f"Decryption stream corrupted: {e}")
            return ""