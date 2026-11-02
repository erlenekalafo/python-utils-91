import hashlib
import hmac
from typing import Union

SATOSHIS_PER_BTC = 100_000_000
GWEI_PER_ETH = 1_000_000_000


def btc_to_satoshi(btc_amount: Union[int, float]) -> int:
    """Convert Bitcoin amount to Satoshis."""
    if btc_amount < 0:
        raise ValueError("Amount cannot be negative")
    return int(round(btc_amount * SATOSHIS_PER_BTC))


def satoshi_to_btc(satoshi_amount: int) -> float:
    """Convert Satoshis to Bitcoin amount."""
    if satoshi_amount < 0:
        raise ValueError("Amount cannot be negative")
    return satoshi_amount / SATOSHIS_PER_BTC


def eth_to_gwei(eth_amount: Union[int, float]) -> int:
    """Convert Ether amount to Gwei."""
    if eth_amount < 0:
        raise ValueError("Amount cannot be negative")
    return int(round(eth_amount * GWEI_PER_ETH))


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate crypto wallet address for UI display."""
    if not address or len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def create_hmac_signature(secret: str, message: str, algorithm: str = "sha256") -> str:
    """Generate HMAC signature for API request authentication."""
    hash_func = getattr(hashlib, algorithm.lower(), None)
    if hash_func is None:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
    return hmac.new(
        secret.encode("utf-8"),
        message.encode("utf-8"),
        hash_func
    ).hexdigest()
