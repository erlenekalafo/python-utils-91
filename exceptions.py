class CryptoError(Exception):
    """Base class for exceptions in this module."""
    pass

class InsufficientFundsError(CryptoError):
    """Raised when an account has insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds: Available {balance}, required {amount}."
        super().__init__(self.message)

class InvalidTransactionError(CryptoError):
    """Raised when a transaction is invalid."""
    def __init__(self, transaction):
        self.transaction = transaction
        self.message = f"Invalid transaction: {transaction}."
        super().__init__(self.message)

class NetworkError(CryptoError):
    """Raised for network-related issues."""
    def __init__(self, url, status_code):
        self.url = url
        self.status_code = status_code
        self.message = f"Network error at {url}, status code: {status_code}."
        super().__init__(self.message)