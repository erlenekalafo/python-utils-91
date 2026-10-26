import hashlib
from typing import Union


def sanitize_hex(hex_str: str) -> str:
    """Strip 0x prefix and ensure even length hex string."""
    cleaned = hex_str.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]
    if len(cleaned) % 2 != 0:
        cleaned = "0" + cleaned
    return cleaned


def btc_to_satoshi(btc_amount: Union[float, int, str]) -> int:
    """Convert BTC amount to satoshis accurately."""
    return int(round(float(btc_amount) * 100_000_000))


def satoshi_to_btc(sat_amount: int) -> float:
    """Convert satoshis to BTC float representation."""
    return sat_amount / 100_000_000


def eth_to_wei(eth_amount: Union[float, int, str]) -> int:
    """Convert ETH amount to Wei integer."""
    return int(round(float(eth_amount) * 10**18))


def wei_to_eth(wei_amount: int) -> float:
    """Convert Wei integer to ETH float."""
    return wei_amount / 10**18


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    """Format blockchain address for display truncation."""
    if not address or len(address) <= (leading + trailing):
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def double_sha256(data: bytes) -> bytes:
    """Compute Bitcoin-style double SHA-256 hash."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()
