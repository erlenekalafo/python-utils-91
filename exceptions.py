class CryptoError(Exception):
    """Base class for all exceptions related to cryptocurrency operations."""
    pass

class InsufficientFundsError(CryptoError):
    """Raised when a transaction exceeds available funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: Available {balance}, Requested {amount}')

class InvalidTransactionError(CryptoError):
    """Raised when a transaction is invalid."""
    def __init__(self, message):
        self.message = message
        super().__init__(f'Invalid transaction: {message}')

class NetworkError(CryptoError):
    """Raised when there is a network issue."""
    def __init__(self, message):
        self.message = message
        super().__init__(f'Network error: {message}')