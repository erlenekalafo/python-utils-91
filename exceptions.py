class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class ValidationError(CustomError):
    """Raised when validation fails"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when a required item is not found"""
    def __init__(self, item):
        self.message = f'{item} not found'
        super().__init__(self.message)

class DatabaseError(CustomError):
    """Raised for database related errors"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)