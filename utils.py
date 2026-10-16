import hashlib
import hmac
import json
from typing import Any, Dict

def generate_signature(api_secret: str, message: str) -> str:
    """Generates a HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def normalize_crypto_payload(data: Dict[str, Any]) -> str:
    """Sorts keys and returns compact JSON string."""
    return json.dumps(data, sort_keys=True, separators=(',', ':'))

def validate_transaction_data(data: Dict[str, Any]) -> bool:
    """Ensures crypto transaction dict has required keys."""
    required = {'asset', 'amount', 'timestamp'}
    return all(key in data for key in required)

def format_wei_to_eth(wei: int) -> float:
    """Conversion of wei units to ether units."""
    return float(wei) / 10**18