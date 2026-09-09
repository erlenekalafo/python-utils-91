import hashlib
import hmac
import secrets


def hash_data(data: bytes) -> str:
    """Generate SHA-256 hash of the input data."""
    return hashlib.sha256(data).hexdigest()


def compute_hmac(key: bytes, message: bytes) -> str:
    """Compute HMAC-SHA256 signature for a message using a key."""
    return hmac.new(key, message, hashlib.sha256).hexdigest()


def verify_signature(key: bytes, message: bytes, expected_signature: str) -> bool:
    """Verify an HMAC-SHA256 signature securely."""
    actual_signature = compute_hmac(key, message)
    return hmac.compare_digest(actual_signature, expected_signature)


def generate_secure_key(length: int = 32) -> bytes:
    """Generate a cryptographically secure random key."""
    return secrets.token_bytes(length)
