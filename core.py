import hashlib
import hmac
from typing import Dict, Any

def generate_crypto_signature(api_secret: str, payload: str) -> str:
    """Generates HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def sanitize_price_data(raw_data: Dict[str, Any]) -> Dict[str, float]:
    """Converts string-based crypto price values to float."""
    cleaned = {}
    for key, value in raw_data.items():
        try:
            cleaned[key] = float(value)
        except (ValueError, TypeError):
            cleaned[key] = 0.0
    return cleaned

def format_pair_symbol(base: str, quote: str) -> str:
    """Normalizes trading pair symbols to standard format."""
    return f"{base.upper()}_{quote.upper()}"

def validate_order_volume(volume: float, min_limit: float = 0.001) -> bool:
    """Ensures order volume meets exchange requirements."""
    return volume >= min_limit