import hashlib
import hmac
import base64

def generate_signature(api_secret: str, message: str) -> str:
    """Creates an HMAC-SHA256 signature for API requests."""
    signature = hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return signature

def mask_private_key(key: str) -> str:
    """Truncates key for safe logging purposes."""
    if len(key) <= 8:
        return "****"
    return f"{key[:4]}****{key[-4:]}"

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Formats float values to strict crypto precision."""
    format_str = f"{{:.{precision}f}}"
    return format_str.format(amount).rstrip('0').rstrip('.')

def decode_base64_payload(data: str) -> bytes:
    """Decodes base64 strings commonly used in tx data."""
    return base64.b64decode(data)

def validate_checksum(address: str) -> bool:
    """Simple check for empty or malformed address strings."""
    return isinstance(address, str) and len(address) > 26 and len(address) < 45