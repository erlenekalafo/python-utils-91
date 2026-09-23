import hashlib
import hmac
import json
from typing import Dict, Any, Optional

def sign_payload(payload: Dict[str, Any], secret: str) -> str:
    """Generates a HMAC-SHA256 signature for crypto payloads."""
    message = json.dumps(payload, sort_keys=True).encode('utf-8')
    return hmac.new(secret.encode('utf-8'), message, hashlib.sha256).hexdigest()

def validate_order_data(data: Dict[str, Any]) -> bool:
    """Checks required fields for crypto exchange orders."""
    required = {'symbol', 'side', 'quantity', 'price'}
    return all(key in data for key in required)

def format_price(amount: float, precision: int = 8) -> str:
    """Formats crypto amounts to specific decimal precision."""
    return f"{amount:.{precision}f}"

def sanitize_order_book(data: Dict[str, Any]) -> Dict[str, Any]:
    """Cleans raw socket data for downstream processing."""
    return {
        "pair": data.get("s", "UNKNOWN"),
        "bids": data.get("b", []),
        "asks": data.get("a", []),
        "timestamp": data.get("E")
    }