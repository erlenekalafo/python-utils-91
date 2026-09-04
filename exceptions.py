class CryptoUtilError(Exception):
    """Base exception for all python-utils-91 errors."""
    pass


class InvalidInputError(CryptoUtilError):
    """Raised when input validation fails in processing."""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"Invalid '{field}': {message}")


class ValidationError(CryptoUtilError):
    """Raised when data validation against crypto rules fails."""
    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(f"Validation failed: {reason}")


def validate_payload(data: dict) -> None:
    """Validate incoming payload dictionary before processing."""
    if not isinstance(data, dict):
        raise InvalidInputError("payload", "Expected dictionary object")
    
    required_keys = ["address", "amount", "signature"]
    for key in required_keys:
        if key not in data:
            raise InvalidInputError(key, "Missing required key in payload")
        if data[key] is None:
            raise InvalidInputError(key, "Value cannot be None")

    if not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        raise ValidationError("Amount must be a positive number")