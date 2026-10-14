import re
from typing import Optional

class ValidationError(Exception):
    """Custom exception for crypto address validation issues."""
    pass

def validate_crypto_address(address: str, chain_type: str = 'eth') -> bool:
    """
    Validates crypto addresses against pattern matching for supported chains.
    Raises ValidationError on malformed input or unknown chains.
    """
    if not isinstance(address, str) or not address:
        raise ValidationError("Address must be a non-empty string")

    patterns = {
        'eth': r'^0x[a-fA-F0-9]{40}$',
        'btc': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$'
    }

    pattern = patterns.get(chain_type.lower())
    if not pattern:
        raise ValidationError(f"Unsupported chain type: {chain_type}")

    if not re.match(pattern, address):
        raise ValidationError(f"Invalid {chain_type} address format")

    return True

def safe_format_amount(amount: float, precision: int = 8) -> str:
    """
    Safely formats float values to string with defined precision.
    Handles edge cases like negative values or type mismatch.
    """
    try:
        if amount < 0:
            raise ValueError("Negative amount provided")
        return f"{amount:.{precision}f}"
    except (TypeError, ValueError) as e:
        return f"0.{'0' * precision}"