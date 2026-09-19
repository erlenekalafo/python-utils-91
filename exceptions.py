class CryptoError(Exception):
    """Base exception for crypto-related operations."""
    pass

class InsufficientFundsError(CryptoError):
    """Raised when wallet balance is too low."""
    pass

class SignatureVerificationError(CryptoError):
    """Raised when cryptographic signature check fails."""
    pass

class DataFormatError(CryptoError):
    """Raised when input data is malformed or invalid."""
    pass

class NetworkTimeoutError(CryptoError):
    """Raised when node connectivity times out."""
    pass

class RateLimitError(CryptoError):
    """Raised when exceeding API request limits."""
    pass

def handle_crypto_exception(e: Exception) -> str:
    """Converts custom crypto exceptions to human-readable strings."""
    if isinstance(e, CryptoError):
        return f"Crypto operation failed: {str(e)}"
    return "An unexpected system error occurred."