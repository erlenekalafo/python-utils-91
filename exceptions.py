class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class NotFoundError(CustomError):
    """Exception raised for not found errors"""
    def __init__(self, message="Item not found."):
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors"""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f'{field}: {message}')

class ConnectionError(CustomError):
    """Exception raised for connection errors"""
    def __init__(self, message="Connection failed."):
        self.message = message
        super().__init__(self.message)