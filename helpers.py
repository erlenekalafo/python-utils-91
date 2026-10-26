import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, message: str) -> str:
    """Generates an HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def sanitize_order_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values and ensures proper numeric formatting."""
    sanitized = {
        k: (str(v) if isinstance(v, float) else v)
        for k, v in data.items() 
        if v is not None
    }
    return sanitized

def format_crypto_pair(base: str, quote: str) -> str:
    """Standardizes trading pair naming conventions."""
    return f"{base.upper()}/{quote.upper()}"

def calculate_order_hash(order_id: str, timestamp: int) -> str:
    """Creates a unique hash for idempotency checks."""
    payload = f"{order_id}:{timestamp}"
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()