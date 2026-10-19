import hashlib
import hmac
from decimal import Decimal
from typing import Union

# Unit conversion constants
SATOSHI_PER_BTC = Decimal("100000000")
WEI_PER_ETH = Decimal("1000000000000000000")


def btc_to_satoshi(btc_amount: Union[int, float, str, Decimal]) -> int:
    """Convert BTC amount to Satoshi integer."""
    amount = Decimal(str(btc_amount))
    return int(amount * SATOSHI_PER_BTC)


def satoshi_to_btc(satoshi_amount: int) -> Decimal:
    """Convert Satoshi integer to BTC Decimal."""
    return Decimal(satoshi_amount) / SATOSHI_PER_BTC


def eth_to_wei(eth_amount: Union[int, float, str, Decimal]) -> int:
    """Convert ETH amount to Wei integer."""
    amount = Decimal(str(eth_amount))
    return int(amount * WEI_PER_ETH)


def wei_to_eth(wei_amount: int) -> Decimal:
    """Convert Wei integer to ETH Decimal."""
    return Decimal(wei_amount) / WEI_PER_ETH


def double_sha256(data: bytes) -> bytes:
    """Compute double SHA-256 hash commonly used in Bitcoin."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def generate_hmac_sha256(key: bytes, message: bytes) -> str:
    """Generate hex-encoded HMAC-SHA256 signature for API requests."""
    return hmac.new(key, message, hashlib.sha256).hexdigest()
