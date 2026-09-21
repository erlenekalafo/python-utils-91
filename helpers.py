import hashlib
import hmac
import time
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    """Generates an HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_order_params(symbol: str, side: str, amount: float) -> Dict[str, Any]:
    """Standardizes order parameters for exchange communication."""
    return {
        "symbol": symbol.upper(),
        "side": side.lower(),
        "amount": float(amount),
        "timestamp": int(time.time() * 1000)
    }

def sanitize_price(price: float, precision: int = 8) -> float:
    """Truncates price to specific decimal precision for crypto."""
    factor = 10 ** precision
    return int(price * factor) / factor

def validate_crypto_address(address: str) -> bool:
    """Basic length and alphanumeric validation for addresses."""
    if not address or len(address) < 26 or len(address) > 42:
        return False
    return address.isalnum()