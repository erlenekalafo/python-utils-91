class CryptoUtilsError(Exception):
    """Base exception for the crypto-utils-91 package."""
    pass

class InvalidKeyError(CryptoUtilsError):
    """Raised when an encryption key is malformed."""
    pass

class DecryptionFailure(CryptoUtilsError):
    """Raised when decryption fails due to corrupted data."""
    pass

class RateLimitExceeded(CryptoUtilsError):
    """Raised when API request thresholds are hit."""
    pass

def handle_crypto_error(err: Exception) -> None:
    """Centralized error mapping for cryptographic operations."""
    if isinstance(err, (InvalidKeyError, DecryptionFailure)):
        # Log security-sensitive failures internally
        print(f"Security Alert: {err}")
    elif isinstance(err, RateLimitExceeded):
        print("Backing off due to rate limits...")
    else:
        print(f"Unexpected error: {err}")
        raise err