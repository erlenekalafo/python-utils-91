import hashlib
import hmac
import time
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    """Generates HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def normalize_order_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Standardizes incoming crypto order dictionaries."""
    return {
        "symbol": str(data.get("s", "")).upper(),
        "price": float(data.get("p", 0.0)),
        "quantity": float(data.get("q", 0.0)),
        "side": str(data.get("S", "")).lower(),
        "timestamp": int(data.get("t", time.time() * 1000))
    }

def validate_checksum(data: str, expected_hash: str) -> bool:
    """Verifies data integrity using SHA256 checksums."""
    actual_hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hmac.compare_digest(actual_hash, expected_hash)