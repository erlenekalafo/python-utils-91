import hashlib
import hmac
import json
from typing import Any, Dict, Optional

def sign_payload(payload: Dict[str, Any], secret: str) -> str:
    """Generates an HMAC-SHA256 signature for crypto payloads."""
    message = json.dumps(payload, sort_keys=True).encode('utf-8')
    signature = hmac.new(
        secret.encode('utf-8'),
        message,
        hashlib.sha256
    ).hexdigest()
    return signature

def validate_order_data(data: Dict[str, Any]) -> bool:
    """Basic validation for crypto order dictionary structure."""
    required_fields = {'symbol', 'side', 'quantity', 'price'}
    return all(field in data for field in required_fields)

def sanitize_crypto_amount(amount: Any) -> float:
    """Converts various input formats to a float."""
    try:
        return float(amount)
    except (ValueError, TypeError):
        return 0.0

def format_response(status: str, data: Optional[Dict] = None) -> Dict[str, Any]:
    """Standardized response object for crypto operations."""
    return {
        "status": status,
        "payload": data or {},
        "version": "python-utils-91-1.0"
    }