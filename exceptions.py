class CryptoError(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidAddressError(CryptoError):
    """Raised when an address is invalid."""
    def __init__(self, address):
        self.address = address
        super().__init__(f'Invalid blockchain address: {address}')


class InsufficientFundsError(CryptoError):
    """Raised when a wallet has insufficient funds."""
    def __init__(self, available, required):
        self.available = available
        self.required = required
        super().__init__(f'Insufficient funds: available={available}, required={required}')


class TransactionError(CryptoError):
    """Raised when a transaction fails."""
    def __init__(self, transaction_id, message):
        self.transaction_id = transaction_id
        self.message = message
        super().__init__(f'Transaction {transaction_id} failed: {message}')


if __name__ == '__main__':
    try:
        raise InvalidAddressError('123xyz')
    except CryptoError as e:
        print(e)
    
    try:
        raise InsufficientFundsError(0.5, 1.0)
    except CryptoError as e:
        print(e)
    
    try:
        raise TransactionError('tx123abc', 'Network timeout')
    except CryptoError as e:
        print(e)