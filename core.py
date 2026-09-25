import hashlib
import hmac
from typing import Dict, Optional

class CryptoProcessor:
    def __init__(self, secret: str):
        self._secret = secret.encode('utf-8')

    def generate_signature(self, message: str) -> str:
        """Generate HMAC-SHA256 signature for payload."""
        return hmac.new(
            self._secret, 
            message.encode('utf-8'), 
            hashlib.sha256
        ).hexdigest()

    def verify_payload(self, message: str, signature: str) -> bool:
        """Constant-time verification of HMAC signatures."""
        expected = self.generate_signature(message)
        return hmac.compare_digest(expected, signature)

class DataSanitizer:
    @staticmethod
    def clean_payload(data: Dict) -> Dict:
        """Strip empty values and normalize keys for crypto ops."""
        return {k: v for k, v in data.items() if v is not None}

def process_auth(payload: Dict, secret: str, signature: str) -> Optional[bool]:
    """Orchestrator for crypto verification workflow."""
    processor = CryptoProcessor(secret)
    sanitized = DataSanitizer.clean_payload(payload)
    
    # Convert dict to string representation for signing
    message = str(sorted(sanitized.items()))
    return processor.verify_payload(message, signature)