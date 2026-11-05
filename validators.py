import re
from typing import Any, Optional

# regex patterns for crypto inputs
ADDRESS_PATTERN = re.compile(r'^(0x)?[a-fA-F0-9]{40}$')
HASH_PATTERN = re.compile(r'^[a-fA-F0-9]{64}$')

class InputValidationError(Exception):
    """Custom exception for validation failures"""
    pass

def validate_crypto_address(address: str) -> bool:
    """Check if string is a valid hexadecimal address"""
    if not ADDRESS_PATTERN.match(address):
        raise InputValidationError(f"Invalid address format: {address}")
    return True

def validate_tx_hash(tx_hash: str) -> bool:
    """Check if string is a valid sha256 hash"""
    if not HASH_PATTERN.match(tx_hash):
        raise InputValidationError(f"Invalid transaction hash: {tx_hash}")
    return True

def sanitize_numeric_input(value: Any) -> float:
    """Ensure input is a positive decimal number"""
    try:
        casted = float(value)
        if casted < 0:
            raise ValueError
        return casted
    except (TypeError, ValueError):
        raise InputValidationError(f"Invalid numeric value provided: {value}")

def validate_processing_payload(payload: dict) -> None:
    """Main validator for processing pipeline payloads"""
    required_keys = {'address', 'amount', 'tx_hash'}
    if not required_keys.issubset(payload.keys()):
        raise InputValidationError("Missing required payload keys")
    
    validate_crypto_address(payload['address'])
    validate_tx_hash(payload['tx_hash'])
    sanitize_numeric_input(payload['amount'])