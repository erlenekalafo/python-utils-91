import hashlib
import hmac
import time
from typing import Dict, Any

class CryptoProcessor:
    def __init__(self, secret: str):
        self._secret = secret.encode('utf-8')

    def generate_signature(self, payload: str) -> str:
        """Generates HMAC-SHA256 signature for API payloads."""
        return hmac.new(
            self._secret,
            payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def verify_timestamp(self, timestamp: float, window: int = 30) -> bool:
        """Checks if request timestamp is within tolerance window."""
        return abs(time.time() - timestamp) <= window

    def sanitize_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Removes sensitive keys from dictionary objects."""
        sensitive_keys = {'api_key', 'private_key', 'secret'}
        return {k: v for k, v in data.items() if k not in sensitive_keys}

    def format_request_body(self, data: Dict[str, Any]) -> str:
        """Sorts and formats dictionary to string for signing."""
        return '&'.join([f"{k}={v}" for k, v in sorted(data.items())])