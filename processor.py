import hashlib
import hmac
import base64
import json

def generate_signature(secret: str, message: str) -> str:
    """Generates HMAC-SHA256 signature for crypto API requests."""
    return hmac.new(
        secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_payload(data: dict) -> str:
    """Sorts keys and serializes payload to JSON string."""
    return json.dumps(data, sort_keys=True, separators=(',', ':'))

def encode_base64(data: str) -> str:
    """Converts string data to base64 encoded format."""
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def validate_ticker(ticker: str) -> bool:
    """Verifies crypto ticker formatting conventions."""
    if not ticker or len(ticker) < 2 or len(ticker) > 10:
        return False
    return ticker.isalnum()

def calculate_fee(amount: float, rate: float = 0.001) -> float:
    """Calculates trading fee based on fixed rate."""
    return round(amount * rate, 8)