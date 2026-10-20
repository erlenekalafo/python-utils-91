import hashlib
import hmac
from typing import Dict, Any

def generate_signature(secret: str, payload: str) -> str:
    """
    Generates an HMAC-SHA256 signature for API requests.

    Args:
        secret: The shared secret key.
        payload: The message body to sign.

    Returns:
        Hexadecimal representation of the HMAC signature.
    """
    return hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def sanitize_order_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Filters out empty values from crypto order parameters.

    Args:
        params: Dictionary of raw order inputs.

    Returns:
        Cleaned dictionary with only non-empty entries.
    """
    return {k: v for k, v in params.items() if v is not None}

def format_price(amount: float, precision: int = 8) -> str:
    """
    Formats crypto currency amounts to specific decimal precision.

    Args:
        amount: The numeric price value.
        precision: Number of decimal places.

    Returns:
        Formatted string representation of the price.
    """
    return f"{amount:.{precision}f}"