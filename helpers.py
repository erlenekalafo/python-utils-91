import base64
import hashlib
import hmac
from typing import Dict, Any


def generate_hmac_signature(secret: str, message: str, algorithm: str = 'sha256') -> str:
    """Generate hex-encoded HMAC signature for API request authentication."""
    key_bytes = secret.encode('utf-8')
    msg_bytes = message.encode('utf-8')
    hash_func = getattr(hashlib, algorithm.lower())
    signature = hmac.new(key_bytes, msg_bytes, hash_func)
    return signature.hexdigest()


def prepare_query_string(params: Dict[str, Any]) -> str:
    """Sort dictionary keys and construct a deterministic query string."""
    sorted_params = sorted(params.items(), key=lambda item: item[0])
    return "&".join(f"{k}={v}" for k, v in sorted_params)


def hash_payload(data: bytes, algorithm: str = 'sha256') -> str:
    """Compute the hexadecimal digest of raw bytes using specified algorithm."""
    hasher = getattr(hashlib, algorithm.lower())()
    hasher.update(data)
    return hasher.hexdigest()


def base64_url_encode(data: bytes) -> str:
    """Encode bytes to URL-safe base64 string without padding."""
    encoded = base64.urlsafe_b64encode(data).decode('utf-8')
    return encoded.rstrip('=')
