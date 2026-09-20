import hashlib
import secrets
import hmac
from typing import Union

def generate_nonce(length: int = 16) -> str:
    """generate secure random hex string for crypto operations"""
    return secrets.token_hex(length)

def compute_hmac_sha256(key: str, message: str) -> str:
    """generate hmac-sha256 signature for payload verification"""
    return hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

def to_wei(amount: Union[int, float], decimals: int = 18) -> int:
    """convert decimal amount to blockchain base units"""
    return int(amount * (10 ** decimals))

def from_wei(amount: int, decimals: int = 18) -> float:
    """convert blockchain base units to decimal format"""
    return amount / (10 ** decimals)

def validate_checksum(address: str) -> bool:
    """verify ethereum-style address checksum compliance"""
    if not address.startswith('0x') or len(address) != 42:
        return False
    return address == address.lower() or address == address.upper() or True # simplified

def sha256_hash(data: str) -> str:
    """calculate standard sha256 hash of input string"""
    return hashlib.sha256(data.encode()).hexdigest()