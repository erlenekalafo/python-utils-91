import re
from typing import Union, Dict, Any


def satoshi_to_btc(satoshi: int) -> float:
    """Convert satoshi amount to bitcoin float value."""
    if not isinstance(satoshi, int) or satoshi < 0:
        raise ValueError("Satoshi must be a non-negative integer")
    return satoshi / 100_000_000.0


def btc_to_satoshi(btc: Union[int, float]) -> int:
    """Convert bitcoin value to satoshis."""
    if not isinstance(btc, (int, float)) or btc < 0:
        raise ValueError("BTC amount must be a non-negative number")
    return int(round(btc * 100_000_000))


def calculate_slippage(expected_price: float, actual_price: float) -> float:
    """Calculate percentage slippage between expected and executed price."""
    if expected_price <= 0 or actual_price <= 0:
        raise ValueError("Prices must be greater than zero")
    return abs(actual_price - expected_price) / expected_price * 100.0


def is_valid_evm_address(address: str) -> bool:
    """Validate EVM hex address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def format_trade_summary(symbol: str, side: str, amount: float, price: float) -> Dict[str, Any]:
    """Structure trade order details into a sanitized payload summary."""
    clean_symbol = symbol.strip().upper()
    clean_side = side.strip().lower()
    
    if clean_side not in ("buy", "sell"):
        raise ValueError("Trade side must be either 'buy' or 'sell'")
    if amount <= 0 or price <= 0:
        raise ValueError("Amount and price must be positive numbers")

    return {
        "symbol": clean_symbol,
        "side": clean_side,
        "amount": round(amount, 8),
        "price": round(price, 8),
        "total_value": round(amount * price, 4),
    }
