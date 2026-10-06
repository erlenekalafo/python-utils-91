from decimal import Decimal, InvalidOperation
from typing import Dict, Any, Optional, Union

# Crypto utility helpers with strict type checking and defensive error handling


def satoshi_to_btc(sats: Union[int, str, Decimal]) -> Decimal:
    """Converts Satoshi value to BTC Decimal safely handling malformed inputs."""
    try:
        sats_dec = Decimal(str(sats))
        if sats_dec < 0:
            raise ValueError("Satoshi amount cannot be negative")
        if sats_dec % 1 != 0:
            raise ValueError("Satoshi amount must be a whole integer")
        return sats_dec / Decimal("100000000")
    except (InvalidOperation, TypeError) as err:
        raise ValueError(f"Invalid satoshi value provided: {sats}") from err


def calculate_price_change(
    old_price: Union[float, str, Decimal],
    new_price: Union[float, str, Decimal]
) -> Decimal:
    """Calculates percentage price change, handling zero or negative baseline edge cases."""
    try:
        old_dec = Decimal(str(old_price))
        new_dec = Decimal(str(new_price))

        if old_dec <= 0:
            return Decimal("0.0")

        change = ((new_dec - old_dec) / old_dec) * Decimal("100")
        return change.quantize(Decimal("0.01"))
    except (InvalidOperation, TypeError):
        return Decimal("0.0")


def parse_ticker_rate(
    payload: Dict[str, Any], key: str, default: Optional[Decimal] = None
) -> Decimal:
    """Safely parses exchange rate values from raw dict payload edge cases."""
    fallback = default if default is not None else Decimal("0.0")
    if not isinstance(payload, dict):
        return fallback

    val = payload.get(key)
    if val is None:
        return fallback

    try:
        parsed = Decimal(str(val))
        return parsed if parsed >= 0 else fallback
    except (InvalidOperation, TypeError):
        return fallback
