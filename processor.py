import hashlib
import hmac
import base64
import json

def generate_signature(api_secret: str, message: str) -> str:
    """Creates an HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def encode_payload(data: dict) -> str:
    """Serializes dictionary to a base64 encoded JSON string."""
    json_str = json.dumps(data, sort_keys=True)
    return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

def decode_payload(encoded_str: str) -> dict:
    """Decodes a base64 string back into a dictionary."""
    decoded = base64.b64decode(encoded_str.encode('utf-8'))
    return json.loads(decoded.decode('utf-8'))

def validate_checksum(data: str, checksum: str) -> bool:
    """Verifies data integrity using SHA256 hashing."""
    calculated = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hmac.compare_digest(calculated, checksum)

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Formats float values to fixed-precision strings."""
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')