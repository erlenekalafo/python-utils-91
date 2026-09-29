import re
from typing import Optional

def validate_bitcoin_address(address: str) -> bool:
    """
    Validate a standard Bitcoin P2PKH/P2SH address format.
    
    Args:
        address: The string representation of the BTC address.

    Returns:
        bool: True if the address matches the base58 regex.
    """
    pattern = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
    return bool(re.match(pattern, address))

def validate_hex_key(key: str) -> bool:
    """
    Validate that a string is a valid hexadecimal private key format.
    
    Args:
        key: The hex string to validate.

    Returns:
        bool: True if the key length is valid and characters are hex.
    """
    return bool(re.fullmatch(r'[0-9a-fA-F]{64}', key))

def sanitize_currency_code(code: str) -> Optional[str]:
    """
    Normalize and validate crypto currency ticker symbols.
    
    Args:
        code: Ticker string like 'BTC' or 'eth'.

    Returns:
        str: Uppercase validated code or None if invalid.
    """
    clean_code = code.strip().upper()
    if re.fullmatch(r'[A-Z]{2,6}', clean_code):
        return clean_code
    return None