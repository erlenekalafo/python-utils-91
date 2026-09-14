class CryptoError(Exception):
    """Base exception for crypto operations."""
    pass

class ValidationError(CryptoError):
    """Raised when input data validation fails."""
    pass

class ConnectionTimeoutError(CryptoError):
    """Raised when network operations exceed limits."""
    pass

class RateLimitError(CryptoError):
    """Raised when API requests exceed limits."""
    pass

class InsufficientFundsError(CryptoError):
    """Raised during failed transaction validation."""
    pass

def raise_if_invalid(condition: bool, message: str):
    """Helper to raise ValidationError if condition is false."""
    if not condition:
        raise ValidationError(message)

def handle_crypto_exception(e: Exception):
    """Generic logging and re-raising helper."""
    if isinstance(e, CryptoError):
        print(f"[CryptoError]: {e}")
        raise e
    print(f"[UnknownError]: {e}")
    raise CryptoError("An unexpected internal error occurred")