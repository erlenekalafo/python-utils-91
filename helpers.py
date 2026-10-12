from decimal import Decimal
from typing import Union
import re


def btc_to_satoshi(btc_amount: Union[int, float, str, Decimal]) -> int:
    """Convert a Bitcoin amount to Satoshis.

    Args:
        btc_amount: The Bitcoin amount to convert.

    Returns:
        The equivalent amount in Satoshis.

    Raises:
        ValueError: If input cannot be converted to Decimal.
    """
    try:
        decimal_btc = Decimal(str(btc_amount))
        return int(decimal_btc * Decimal("100000000"))
    except Exception as e:
        raise ValueError(f"Invalid BTC amount: {btc_amount}") from e


def satoshi_to_btc(satoshi_amount: int) -> Decimal:
    """Convert a Satoshi amount to Bitcoin Decimal.

    Args:
        satoshi_amount: The integer number of Satoshis.

    Returns:
        The equivalent amount in Bitcoin as a Decimal.
    """
    if not isinstance(satoshi_amount, int):
        raise TypeError("Satoshi amount must be an integer.")
    return Decimal(satoshi_amount) / Decimal("100000000")


def format_crypto_pair(base: str, quote: str) -> str:
    """Format base and quote symbols into a standardized trading pair.

    Args:
        base: The base currency symbol (e.g., 'BTC').
        quote: The quote currency symbol (e.g., 'USDT').

    Returns:
        A normalized trading pair string formatted as 'BASE/QUOTE'.
    """
    clean_base = base.strip().upper()
    clean_quote = quote.strip().upper()
    return f"{clean_base}/{clean_quote}"


def is_valid_evm_address(address: str) -> bool:
    """Verify if a string matches an Ethereum (EVM) address format.

    Args:
        address: The hexadecimal address string to validate.

    Returns:
        True if the address is a valid 42-character hex string.
    """
    if not isinstance(address, str):
        return False
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))
