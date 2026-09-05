class CryptoValidationError(ValueError):
    """Base exception for all cryptography validation errors."""
    pass

class InvalidAddressError(CryptoValidationError):
    """Raised when a cryptocurrency address format is invalid."""
    def __init__(self, address: str, network: str, message: str = None):
        self.address = address
        self.network = network
        self.message = message or f"Invalid {network} address: {address}"
        super().__init__(self.message)

class InvalidKeyError(CryptoValidationError):
    """Raised when a cryptographic key (public/private) is invalid."""
    def __init__(self, key_type: str, message: str = None):
        self.key_type = key_type
        self.message = message or f"Invalid cryptographic {key_type} key format"
        super().__init__(self.message)

class InsufficientFundsError(CryptoValidationError):
    """Raised when a transaction input amount exceeds the balance."""
    def __init__(self, required: float, available: float, message: str = None):
        self.required = required
        self.available = available
        self.message = message or f"Insufficient funds: required {required}, available {available}"
        super().__init__(self.message)