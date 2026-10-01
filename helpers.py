import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    """Generates HMAC-SHA256 signature for crypto API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def sanitize_order_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values and ensures proper types for trading payloads."""
    return {k: v for k, v in data.items() if v is not None}

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Formats float amounts to fixed precision strings."""
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def validate_ticker_format(ticker: str) -> bool:
    """Checks if ticker follows standard BTC-USDT naming convention."""
    return '-' in ticker and ticker.isupper()