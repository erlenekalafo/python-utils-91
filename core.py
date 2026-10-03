import hashlib
import os
from typing import Union


def generate_secure_salt(length: int = 16) -> bytes:
    """Generate a cryptographically secure random salt."""
    if length < 8:
        raise ValueError("Salt length must be at least 8 bytes.")
    return os.urandom(length)


def hash_sha256(data: Union[str, bytes]) -> str:
    """Compute the SHA-256 hash of the input data as a hex string."""
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def derive_key(password: str, salt: bytes, iterations: int = 100000, key_len: int = 32) -> bytes:
    """Derive a cryptographic key using PBKDF2-HMAC-SHA256."""
    if not password:
        raise ValueError("Password cannot be empty.")
    password_bytes = password.encode('utf-8')
    return hashlib.pbkdf2_hmac('sha256', password_bytes, salt, iterations, dklen=key_len)


def xor_bytes(b1: bytes, b2: bytes) -> bytes:
    """Perform a bitwise XOR operation between two byte sequences."""
    if len(b1) != len(b2):
        raise ValueError("Byte sequences must be of equal length.")
    return bytes(a ^ b for a, b in zip(b1, b2))


def bytes_to_hex(data: bytes) -> str:
    """Convert bytes to a clean lowercase hex string."""
    return data.hex().lower()


def hex_to_bytes(hex_str: str) -> bytes:
    """Convert hex string to bytes, handling potential 0x prefix."""
    clean_hex = hex_str.lower()
    if clean_hex.startswith('0x'):
        clean_hex = clean_hex[2:]
    return bytes.fromhex(clean_hex)
