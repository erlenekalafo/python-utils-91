import hashlib
import hmac
import time
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    """Creates an HMAC-SHA256 signature for API authentication."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def normalize_crypto_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Standardizes incoming crypto price updates to common format."""
    return {
        "symbol": str(data.get("s", "")).upper(),
        "price": float(data.get("p", 0.0)),
        "quantity": float(data.get("q", 0.0)),
        "timestamp": int(data.get("t", time.time() * 1000)),
        "source": "exchange_v1"
    }

def validate_order_volume(volume: float, min_limit: float = 0.001) -> bool:
    """Ensures trading volume meets minimum exchange requirements."""
    try:
        return float(volume) >= min_limit
    except (ValueError, TypeError):
        return False