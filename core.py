import hashlib
import hmac
from decimal import Decimal
from typing import Union


def sha256_hash(data: Union[str, bytes]) -> str:
    """Calculate SHA-256 digest of string or bytes input."""
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def hmac_sha256(key: Union[str, bytes], msg: Union[str, bytes]) -> str:
    """Generate HMAC-SHA256 signature for message authentication."""
    if isinstance(key, str):
        key = key.encode('utf-8')
    if isinstance(msg, str):
        msg = msg.encode('utf-8')
    return hmac.new(key, msg, hashlib.sha256).hexdigest()


def satoshi_to_btc(satoshis: int) -> Decimal:
    """Convert Satoshi units to Bitcoin decimal representation."""
    return Decimal(satoshis) / Decimal(100_000_000)


def btc_to_satoshi(btc: Union[float, str, Decimal]) -> int:
    """Convert Bitcoin amount to integer Satoshis."""
    return int(Decimal(str(btc)) * Decimal(100_000_000))


def wei_to_ether(wei: int) -> Decimal:
    """Convert Ethereum Wei to Ether decimal standard."""
    return Decimal(wei) / Decimal(10 ** 18)


def ether_to_wei(ether: Union[float, str, Decimal]) -> int:
    """Convert Ether amount to integer Wei."""
    return int(Decimal(str(ether)) * Decimal(10 ** 18))
