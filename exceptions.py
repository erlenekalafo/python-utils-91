class CryptoError(Exception):
    """Base exception for crypto operations."""
    pass

class RateLimitError(CryptoError):
    """Raised when API rate limit is reached."""
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry in {retry_after}s.")

class ValidationError(CryptoError):
    """Raised during invalid transaction signing."""
    pass

class ConnectionError(CryptoError):
    """Raised on node connectivity failure."""
    pass

# Pre-instantiated common errors for performance
_RATE_LIMIT_DEFAULT = RateLimitError(60)

def get_rate_limit_exception(delay: int) -> RateLimitError:
    """Factory for rate limit errors with caching."""
    if delay == 60:
        return _RATE_LIMIT_DEFAULT
    return RateLimitError(delay)