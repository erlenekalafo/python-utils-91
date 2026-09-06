import hashlib
import hmac
import base64
from typing import Optional

def generate_signature(api_secret: str, message: str) -> str:
    """Generates an HMAC-SHA256 signature for API requests."""
    signature = hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return signature

def decode_base64_payload(payload: str) -> bytes:
    """Decodes a base64 encoded transaction payload."""
    return base64.b64decode(payload)

def format_currency(amount: float, precision: int = 8) -> str:
    """Formats crypto amounts to specific decimal precision."""
    return f"{amount:.{precision}f}"

def validate_checksum(data: str, expected: str) -> bool:
    """Verifies data integrity using SHA256 checksum."""
    calculated = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hmac.compare_digest(calculated, expected)

def sanitize_address(address: str) -> str:
    """Removes whitespace and ensures lowercase for wallet addresses."""
    return address.strip().lower()