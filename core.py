import hashlib
import hmac
import secrets


def generate_secure_salt(length: int = 16) -> str:
    """Generates a cryptographically secure random hexadecimal salt."""
    if length <= 0:
        raise ValueError("Salt length must be a positive integer.")
    return secrets.token_hex(length)


def hash_payload(payload: str, salt: str = "") -> str:
    """Hashes a payload with an optional salt using SHA-256."""
    hasher = hashlib.sha256()
    if salt:
        hasher.update(salt.encode("utf-8"))
    hasher.update(payload.encode("utf-8"))
    return hasher.hexdigest()


def generate_hmac(key: str, message: str) -> str:
    """Generates an HMAC-SHA256 signature for a message using a secret key."""
    if not key:
        raise ValueError("HMAC key cannot be empty.")
    key_bytes = key.encode("utf-8")
    message_bytes = message.encode("utf-8")
    return hmac.new(key_bytes, message_bytes, hashlib.sha256).hexdigest()


def verify_hmac(key: str, message: str, signature: str) -> bool:
    """Safely compares an HMAC-SHA256 signature to prevent timing attacks."""
    expected_signature = generate_hmac(key, message)
    # Use compare_digest to mitigate timing attacks
    return hmac.compare_digest(expected_signature, signature)