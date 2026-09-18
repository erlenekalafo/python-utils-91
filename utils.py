import hashlib
import hmac
import base64
from typing import Optional

class CryptoUtils:
    """Collection of helper methods for cryptographic operations."""

    @staticmethod
    def generate_hmac(key: str, message: str, algorithm: str = 'sha256') -> str:
        """Generates a HMAC signature for data integrity verification."""
        return hmac.new(
            key.encode('utf-8'),
            message.encode('utf-8'),
            getattr(hashlib, algorithm)
        ).hexdigest()

    @staticmethod
    def encode_base64(data: str) -> str:
        """Encodes string data to base64 format."""
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')

    @staticmethod
    def decode_base64(encoded_data: str) -> str:
        """Decodes base64 string data to utf-8 format."""
        return base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')

    @staticmethod
    def secure_compare(val1: str, val2: str) -> bool:
        """Constant-time string comparison to prevent timing attacks."""
        return hmac.compare_digest(val1, val2)

def hash_payload(data: str, salt: Optional[str] = None) -> str:
    """Helper for generating SHA-256 hashes with optional salt."""
    payload = (data + (salt or '')).encode('utf-8')
    return hashlib.sha256(payload).hexdigest()