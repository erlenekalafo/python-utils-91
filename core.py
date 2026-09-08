import decimal
from typing import Union, Dict

def normalize_crypto_amount(amount: Union[str, float, int], precision: int = 8) -> decimal.Decimal:
    """Converts raw crypto inputs to a precise decimal for calculation."""
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_DOWN
    
    try:
        value = decimal.Decimal(str(amount))
        return value.quantize(decimal.Decimal(10) ** -precision)
    except (decimal.InvalidOperation, ValueError) as e:
        raise ValueError(f"Invalid crypto amount format: {amount}") from e

def format_order_payload(symbol: str, side: str, amount: decimal.Decimal, price: decimal.Decimal) -> Dict:
    """Constructs a standardized payload for exchange API requests."""
    return {
        "symbol": symbol.upper(),
        "side": side.lower(),
        "quantity": str(amount),
        "price": str(price),
        "timestamp": "auto"
    }

def calculate_position_value(quantity: decimal.Decimal, price: decimal.Decimal) -> decimal.Decimal:
    """Computes the total fiat value of a position."""
    return (quantity * price).quantize(decimal.Decimal("0.01"))