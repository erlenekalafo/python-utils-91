from typing import Any, Dict

class ValidationError(ValueError):
    """Raised when input validation fails for crypto payloads."""
    pass

def validate_crypto_payload(payload: Dict[str, Any]) -> bool:
    """
    Validate incoming transaction payload structure and data types.
    Ensures required fields exist and values are within expected ranges.
    """
    if not isinstance(payload, dict):
        raise ValidationError("Payload must be a dictionary")
    
    required_fields = {"sender": str, "recipient": str, "amount": (int, float), "nonce": int}
    
    for field, expected_type in required_fields.items():
        if field not in payload:
            raise ValidationError(f"Missing required field: {field}")
        
        if not isinstance(payload[field], expected_type):
            raise ValidationError(
                f"Invalid type for {field}: expected {expected_type}, got {type(payload[field])}"
            )
            
    if payload["amount"] <= 0:
        raise ValidationError("Transaction amount must be greater than zero")
        
    if payload["nonce"] < 0:
        raise ValidationError("Nonce cannot be negative")
        
    return True
