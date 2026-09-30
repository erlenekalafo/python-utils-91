import hashlib
import secrets
from typing import Union


def generate_secure_salt(length: int = 16) -> bytes:
    """
    Generate a cryptographically secure random salt.

    :param length: The size of the salt in bytes.
    :return: A random bytes object of the specified length.
    """
    return secrets.token_bytes(length)


def hash_data(data: Union[str, bytes], algorithm: str = "sha256") -> str:
    """
    Hash the given data using the specified cryptographic hash algorithm.

    :param data: The input string or bytes to hash.
    :param algorithm: The hashing algorithm to use (e.g., 'sha256', 'sha512').
    :return: The hexadecimal string representation of the hash.
    :raises ValueError: If the specified algorithm is not supported.
    """
    if isinstance(data, str):
        data_bytes = data.encode("utf-8")
    else:
        data_bytes = data

    try:
        hasher = hashlib.new(algorithm)
    except ValueError as e:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}") from e

    hasher.update(data_bytes)
    return hasher.hexdigest()


def derive_key(passphrase: str, salt: bytes, iterations: int = 100000, key_length: int = 32) -> bytes:
    """
    Derive a cryptographic key from a passphrase and a salt using PBKDF2-HMAC-SHA256.

    :param passphrase: The user passphrase as a string.
    :param salt: A cryptographically secure salt.
    :param iterations: The number of iterations for PBKDF2 (default: 100,000).
    :param key_length: The desired length of the derived key in bytes (default: 32).
    :return: The derived key as bytes.
    """
    passphrase_bytes = passphrase.encode("utf-8")
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=passphrase_bytes,
        salt=salt,
        iterations=iterations,
        dklen=key_length
    )
