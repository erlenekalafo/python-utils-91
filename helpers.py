import hashlib
import hmac
import json
import base64
from typing import Any, Dict

def generate_sha256_hash(data: str) -> str:
    """Generate hex digest of input string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def create_hmac_signature(key: str, message: str) -> str:
    """Create HMAC-SHA256 signature for API requests."""
    return hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

def encode_to_base64(data: str) -> str:
    """Encode string to base64 format."""
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def decode_from_base64(encoded: str) -> str:
    """Decode base64 string to original format."""
    return base64.b64decode(encoded.encode('utf-8')).decode('utf-8')

def serialize_json(data: Dict[str, Any]) -> str:
    """Safe JSON serialization for crypto payloads."""
    return json.dumps(data, sort_keys=True, separators=(',', ':'))

def mask_address(address: str, visible: int = 6) -> str:
    """Mask crypto address for logging safety."""
    if len(address) <= visible * 2:
        return address
    return f"{address[:visible]}...{address[-visible:]}"