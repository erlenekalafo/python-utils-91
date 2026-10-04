import hashlib
import hmac
import base64
from typing import Any, Dict

def generate_signature(api_secret: str, message: str) -> str:
    """Generates an HMAC-SHA256 signature for API authentication."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def truncate_address(address: str, length: int = 6) -> str:
    """Shortens a crypto address for display purposes."""
    if len(address) <= length * 2:
        return address
    return f"{address[:length]}...{address[-length:]}"

def normalize_amount(amount: Any, decimals: int = 8) -> float:
    """Converts raw crypto balances to human-readable float format."""
    try:
        return round(float(amount) / (10**decimals), decimals)
    except (TypeError, ValueError):
        return 0.0

def validate_payload_keys(payload: Dict, required_keys: list) -> bool:
    """Ensures all mandatory fields exist in API payloads."""
    return all(key in payload for key in required_keys)