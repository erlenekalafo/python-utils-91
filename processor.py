import hashlib
import hmac
import json
from typing import Dict, Any

class CryptoDataProcessor:
    """Handles cryptographic signature verification and payload normalization."""

    def __init__(self, secret: str):
        self.secret = secret.encode('utf-8')

    def generate_signature(self, payload: Dict[str, Any]) -> str:
        """Creates HMAC-SHA256 signature for data integrity."""
        message = json.dumps(payload, sort_keys=True).encode('utf-8')
        return hmac.new(
            self.secret, 
            message, 
            hashlib.sha256
        ).hexdigest()

    def verify_payload(self, payload: Dict[str, Any], signature: str) -> bool:
        """Validates signature against provided payload data."""
        expected = self.generate_signature(payload)
        return hmac.compare_digest(expected, signature)

    @staticmethod
    def sanitize_price_data(raw_value: Any) -> float:
        """Normalizes crypto price input to float format."""
        try:
            return float(raw_value)
        except (ValueError, TypeError):
            return 0.0

def process_trade_event(processor: CryptoDataProcessor, event: Dict[str, Any], sig: str) -> Dict[str, Any]:
    """Entry point for incoming trade stream processing."""
    if not processor.verify_payload(event, sig):
        raise ValueError("Invalid signature provided for trade event")
        
    event['price'] = processor.sanitize_price_data(event.get('price'))
    return event