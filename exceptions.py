"""Custom exception classes for cryptocurrency and cryptographic utilities."""

from typing import Optional, Any


class CryptoUtilsError(Exception):
    """Base exception for all python-utils-91 module errors."""
    
    def __init__(self, message: str, raw_response: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.raw_response = raw_response

    def __str__(self) -> str:
        if self.raw_response is not None:
            return f"{self.message} (Raw Response: {self.raw_response})"
        return self.message


class KeyVerificationError(CryptoUtilsError):
    """Raised when cryptographic key or signature validation fails."""
    pass


class InvalidAddressError(CryptoUtilsError):
    """Raised when a cryptocurrency wallet address format is invalid."""
    
    def __init__(self, address: str, network: str = "mainnet") -> None:
        self.address = address
        self.network = network
        msg = f"Invalid {network} wallet address format: '{address}'"
        super().__init__(msg)


class RateLimitExceededError(CryptoUtilsError):
    """Raised when exchange or RPC node rate limits are hit."""
    
    def __init__(self, retry_after: float = 0.0) -> None:
        self.retry_after = retry_after
        msg = f"Rate limit exceeded. Retry after {retry_after} seconds."
        super().__init__(msg)


class InsufficientBalanceError(CryptoUtilsError):
    """Raised when an operation requires more balance than available."""
    
    def __init__(self, required: float, available: float, asset: str) -> None:
        self.required = required
        self.available = available
        self.asset = asset
        msg = f"Insufficient {asset} balance: required {required}, available {available}"
        super().__init__(msg)
