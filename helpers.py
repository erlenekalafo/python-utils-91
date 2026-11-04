import hashlib
import hmac
import base64
from typing import Optional

def generate_signature(api_secret: str, message: str) -> str:
    """Creates an HMAC SHA256 signature for API requests."""
    secret_bytes = api_secret.encode('utf-8')
    message_bytes = message.encode('utf-8')
    signature = hmac.new(secret_bytes, message_bytes, hashlib.sha256).hexdigest()
    return signature

def truncate_address(address: str, length: int = 8) -> str:
    """Shortens a crypto address for cleaner display."""
    if len(address) <= length * 2:
        return address
    return f"{address[:length]}...{address[-length:]}"

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Formats floats to fixed precision strings."""
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def decode_base64_key(encoded_key: str) -> bytes:
    """Decodes base64 string to raw key bytes."""
    try:
        return base64.b64decode(encoded_key)
    except Exception:
        raise ValueError("Invalid base64 encoding for key")