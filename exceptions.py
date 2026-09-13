class CryptoUtilsError(Exception):
    """Base exception for the crypto-utils-91 package."""
    pass

class InvalidKeyError(CryptoUtilsError):
    """Raised when an encryption key fails format validation."""
    pass

class DecryptionFailedError(CryptoUtilsError):
    """Raised when the payload is malformed or key is incorrect."""
    pass

class RateLimitExceededError(CryptoUtilsError):
    """Raised when the crypto provider throttles requests."""
    pass

class ProviderConnectionError(CryptoUtilsError):
    """Raised during network-level failures with crypto providers."""
    pass

def handle_crypto_exception(e: Exception) -> None:
    """Standardizes error reporting across crypto modules."""
    if isinstance(e, (InvalidKeyError, DecryptionFailedError)):
        print(f"Security violation detected: {e}")
    elif isinstance(e, (RateLimitExceededError, ProviderConnectionError)):
        print(f"Infrastructure fault reported: {e}")
    else:
        print(f"Unexpected system failure: {e}")
    raise e