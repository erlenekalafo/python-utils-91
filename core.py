import hashlib
import hmac
import time
from typing import Optional

class CryptoEngine:
    def __init__(self, secret: str):
        self.secret = secret.encode('utf-8')

    def generate_signature(self, payload: str) -> str:
        """Generate HMAC-SHA256 signature for API payloads."""
        return hmac.new(
            self.secret,
            payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def verify_timestamp(self, timestamp: float, window: int = 5) -> bool:
        """Verify request timestamp within a specific window."""
        return abs(time.time() - timestamp) <= window

    def hash_data(self, data: str) -> str:
        """Return SHA-256 hex digest of provided string."""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

class SecurityManager:
    @staticmethod
    def sanitize_input(data: str) -> str:
        """Remove potential injection artifacts from input."""
        return data.strip().replace(';', '').replace('--', '')

if __name__ == '__main__':
    engine = CryptoEngine(secret='dev_key_91')
    sig = engine.generate_signature('data_packet')