import hashlib
from typing import Union

SATOSHIS_PER_BTC = 100_000_000


def satoshi_to_btc(satoshis: int) -> float:
    """Convert satoshis to decimal BTC amount."""
    if satoshis < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return satoshis / SATOSHIS_PER_BTC


def btc_to_satoshi(btc: Union[float, int]) -> int:
    """Convert decimal BTC amount to satoshis."""
    if btc < 0:
        raise ValueError("BTC amount cannot be negative")
    return int(round(btc * SATOSHIS_PER_BTC))


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate crypto wallet address for safe display."""
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def double_sha256(data: bytes) -> bytes:
    """Calculate double SHA-256 hash used in Bitcoin protocol."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def is_valid_hex_string(hex_str: str) -> bool:
    """Check if string is a valid even-length hex string."""
    cleaned = hex_str[2:] if hex_str.startswith(("0x", "0X")) else hex_str
    if not cleaned or len(cleaned) % 2 != 0:
        return False
    try:
        int(cleaned, 16)
        return True
    except ValueError:
        return False
