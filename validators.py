import re
from typing import Union

def _is_hex(s: str, length: int = None) -> bool:
    """Internal helper to check hex string."""
    if not isinstance(s, str):
        return False
    if length is not None and len(s) != length:
        return False
    return bool(re.fullmatch(r'[0-9a-fA-F]+', s))

def is_valid_ethereum_address(address: str) -> bool:
    """Validate Ethereum address format.
    Must start with 0x and have 40 hex characters.
    """
    if not isinstance(address, str):
        return False
    if len(address) != 42 or not address.startswith("0x"):
        return False
    return _is_hex(address[2:])

def is_valid_bitcoin_address(address: str) -> bool:
    """Validate Bitcoin address using regex.
    Basic check for common address types.
    """
    if not isinstance(address, str):
        return False
    # P2PKH starts with 1, P2SH with 3
    pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    return bool(re.match(pattern, address))

def is_valid_transaction_hash(tx_hash: str, crypto_type: str = "ethereum") -> bool:
    """Validate crypto transaction hash.
    Ethereum: 66 chars with 0x, Bitcoin: 64 hex chars.
    """
    if not isinstance(tx_hash, str):
        return False
    crypto_type = crypto_type.lower()
    if crypto_type in ["ethereum", "eth"]:
        if len(tx_hash) != 66 or not tx_hash.startswith("0x"):
            return False
        return _is_hex(tx_hash[2:], 64)
    elif crypto_type in ["bitcoin", "btc"]:
        if len(tx_hash) != 64:
            return False
        return _is_hex(tx_hash)
    return False

def validate_amount(amount: Union[str, int, float], min_value: float = 0) -> bool:
    """Check if amount is valid positive number."""
    try:
        value = float(amount)
        return value >= min_value
    except (ValueError, TypeError):
        return False

def is_valid_wallet_address(address: str, crypto: str = "eth") -> bool:
    """General wallet address validator."""
    crypto = crypto.lower()
    if crypto in ["eth", "ethereum"]:
        return is_valid_ethereum_address(address)
    elif crypto in ["btc", "bitcoin"]:
        return is_valid_bitcoin_address(address)
    return False