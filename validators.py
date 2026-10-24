import re
from typing import Union

# Pre-compiled regex patterns for standard crypto formats
ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_REGEX = re.compile(r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-0-9]{39,59})$")
TX_HASH_REGEX = re.compile(r"^(0x)?[a-fA-F0-9]{64}$")


def is_valid_eth_address(address: str) -> bool:
    """Validate Ethereum address format including basic hex structure."""
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_REGEX.match(address))


def is_valid_btc_address(address: str) -> bool:
    """Validate legacy, P2SH, or Bech32 Bitcoin address format."""
    if not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_REGEX.match(address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    """Validate standard 32-byte crypto transaction hash string."""
    if not isinstance(tx_hash, str):
        return False
    return bool(TX_HASH_REGEX.match(tx_hash))


def validate_positive_amount(val: Union[int, float, str]) -> bool:
    """Verify that a transaction amount is a positive number."""
    try:
        amount = float(val)
        return amount > 0
    except (ValueError, TypeError):
        return False
