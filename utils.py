import hashlib
import hmac
import json
from typing import Dict, Any, Optional

def generate_signature(api_secret: str, payload: Dict[str, Any]) -> str:
    """Generates a HMAC-SHA256 signature for API requests."""
    serialized_payload = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    return hmac.new(
        api_secret.encode('utf-8'),
        serialized_payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def sanitize_crypto_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes sensitive fields from crypto transaction logs."""
    sensitive_keys = {'private_key', 'api_key', 'passphrase', 'mnemonic'}
    return {k: v for k, v in data.items() if k not in sensitive_keys}

def format_wei_to_eth(wei_amount: int) -> float:
    """Converts wei units to standard ether decimal format."""
    return float(wei_amount) / 10**18

def validate_transaction_payload(payload: Optional[Dict[str, Any]]) -> bool:
    """Basic validation for crypto transaction dictionaries."""
    if not payload or not isinstance(payload, dict):
        return False
    required_fields = {'amount', 'currency', 'recipient'}
    return required_fields.issubset(payload.keys())