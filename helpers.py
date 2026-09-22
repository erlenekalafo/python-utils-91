import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class CryptoError(Exception):
    """Base exception for crypto-utils-91 operations."""
    pass

def validate_payload(data: Any) -> bool:
    """Ensures input is a non-empty dictionary for cryptographic processing."""
    if not isinstance(data, dict):
        logger.error("Invalid payload type: expected dict")
        return False
    if not data:
        logger.warning("Empty payload received")
        return False
    return True

def safe_decrypt(key: str, encrypted_data: Optional[str]) -> Optional[str]:
    """Attempts decryption with basic integrity checks."""
    try:
        if not key or not encrypted_data:
            raise ValueError("Missing decryption credentials")
        
        # Simulation of decryption logic
        return f"decrypted_{encrypted_data}"
    except ValueError as e:
        logger.error(f"Decryption parameter error: {e}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected crypto failure: {e}")
        return None

def format_address(address: Any) -> str:
    """Sanitizes and formats crypto wallet addresses."""
    try:
        if not isinstance(address, str):
            raise TypeError("Address must be a string")
        return address.strip().lower()
    except TypeError:
        return "0x0000000000000000000000000000000000000000"