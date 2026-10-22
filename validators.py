class CryptoValidationError(Exception):
    """Base exception for crypto processing errors."""
    pass

def validate_payload(data: dict) -> bool:
    """Ensures input payload has required keys and valid types."""
    required_keys = {"address": str, "amount": (int, float), "currency": str}
    
    for key, expected_type in required_keys.items():
        if key not in data:
            raise CryptoValidationError(f"Missing required field: {key}")
        if not isinstance(data[key], expected_type):
            raise CryptoValidationError(f"Invalid type for {key}: expected {expected_type}")
            
    if data["amount"] <= 0:
        raise CryptoValidationError("Amount must be a positive value")
        
    return True

def validate_address(address: str) -> bool:
    """Checks basic address format for crypto transactions."""
    if not (26 <= len(address) <= 35):
        raise CryptoValidationError("Invalid address length for validation")
    if not address.isalnum():
        raise CryptoValidationError("Address must be alphanumeric")
    return True