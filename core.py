import hashlib
import hmac
import base64
import json
from typing import Dict, Any

def generate_signature(api_secret: str, payload: Dict[str, Any]) -> str:
    """Generates HMAC-SHA256 signature for API requests."""
    serialized = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    signature = hmac.new(
        api_secret.encode('utf-8'),
        serialized.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return signature

def decode_base64_json(encoded_data: str) -> Dict[str, Any]:
    """Decodes base64 string into a python dictionary."""
    try:
        decoded = base64.b64decode(encoded_data)
        return json.loads(decoded)
    except (ValueError, TypeError, json.JSONDecodeError) as e:
        return {"error": "decoding_failed", "message": str(e)}

def calculate_checksum(data: bytes) -> str:
    """Calculates SHA-256 checksum for raw data."""
    return hashlib.sha256(data).hexdigest()

if __name__ == '__main__':
    # Example usage for verification
    mock_payload = {"symbol": "BTC-USD", "amount": 1.0}
    sig = generate_signature("secret_key", mock_payload)
    print(f"Generated signature: {sig}")