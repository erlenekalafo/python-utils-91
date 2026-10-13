from decimal import Decimal, InvalidOperation
from typing import Union
import re


class CryptoAmountProcessor:
    """Safely converts and processes cryptocurrency amounts and units."""

    # Standard decimal precision limits for major cryptocurrencies
    PRECISION_MAP = {
        "BTC": 8,
        "ETH": 18,
        "SOL": 9,
        "USDT": 6
    }

    @classmethod
    def to_base_unit(cls, amount: Union[str, int, float], symbol: str) -> int:
        """Converts human-readable amount to smallest unit (e.g., BTC to Satoshis)."""
        symbol = symbol.upper()
        if symbol not in cls.PRECISION_MAP:
            raise ValueError(f"Unsupported crypto symbol: {symbol}")

        # Edge case: Handle None or empty values
        if amount is None or amount == "":
            raise ValueError("Amount cannot be null or empty string")

        # Edge case: Handle float inputs directly to prevent floating point error
        if isinstance(amount, float):
            amount = str(amount)

        try:
            dec_amount = Decimal(str(amount))
        except (InvalidOperation, TypeError) as e:
            raise ValueError(f"Invalid numeric format for amount: {amount}") from e

        # Edge case: Non-finite numbers and negative values
        if dec_amount.is_nan() or dec_amount.is_infinite():
            raise ValueError("Amount must be a finite number")
        if dec_amount < 0:
            raise ValueError("Crypto amount cannot be negative")

        decimals = cls.PRECISION_MAP[symbol]
        multiplier = Decimal(10 ** decimals)
        base_unit = dec_amount * multiplier

        # Edge case: Ensure no fractional sub-units remain beyond allowed precision
        if base_unit % 1 != 0:
            raise ValueError(
                f"Amount exceeds maximum precision of {decimals} decimals for {symbol}"
            )

        return int(base_unit)


def parse_tx_hash(tx_hash: str) -> str:
    """Sanitizes and validates a standard 64-character hex transaction hash."""
    if not isinstance(tx_hash, str):
        raise TypeError("Transaction hash must be a string")

    cleaned = tx_hash.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]

    # Edge case: Malformed hex length or characters
    if not re.fullmatch(r"[0-9a-f]{64}", cleaned):
        raise ValueError("Malformed transaction hash format")

    return f"0x{cleaned}"
