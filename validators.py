import re
from typing import Any

class ValidationError(Exception):
    """Custom exception for crypto address validation issues."""
    pass

def validate_eth_address(address: Any) -> bool:
    """
    Validates Ethereum hex address format.
    Ensures input is a string and matches the expected hex pattern.
    """
    if not isinstance(address, str):
        raise ValidationError(f"Address must be string, got {type(address).__name__}")
    
    # Hex addresses start with 0x followed by 40 hex characters
    pattern = r"^0x[a-fA-F0-9]{40}$"
    
    if not re.match(pattern, address):
        raise ValidationError(f"Invalid Ethereum address format: {address}")
        
    return True

def validate_amount(amount: Any) -> float:
    """
    Validates numerical amount for crypto transactions.
    Ensures value is positive and finite.
    """
    try:
        val = float(amount)
    except (ValueError, TypeError):
        raise ValidationError(f"Amount must be a numeric value, got {amount}")
        
    if val <= 0:
        raise ValidationError("Transaction amount must be greater than zero")
        
    if float('inf') == val:
        raise ValidationError("Transaction amount cannot be infinite")
        
    return val