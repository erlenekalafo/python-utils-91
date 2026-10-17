import re
from typing import Optional


def is_valid_eth_address(address: str) -> bool:
    """Validate if a string is a properly formatted Ethereum address.

    Args:
        address: The string representation of the Ethereum address.

    Returns:
        True if valid hexadecimal string with 0x prefix and length 42, False otherwise.
    """
    if not isinstance(address, str):
        return False
    pattern = re.compile(r"^0x[a-fA-F0-9]{40}$")
    return bool(pattern.match(address))


def is_valid_btc_address(address: str) -> bool:
    """Validate Legacy, SegWit, or Bech32 Bitcoin wallet address.

    Args:
        address: The string representation of the Bitcoin address.

    Returns:
        True if the address matches standard Bitcoin formats, False otherwise.
    """
    if not isinstance(address, str):
        return False
    btc_pattern = re.compile(
        r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-HJ-NP-Z0-9]{8,87})$"
    )
    return bool(btc_pattern.match(address))


def validate_tx_hash(tx_hash: str, expected_length: Optional[int] = 64) -> bool:
    """Verify that a transaction hash conforms to expected hex length.

    Args:
        tx_hash: Transaction hash string, optional '0x' prefix permitted.
        expected_length: Expected character count excluding '0x' prefix.

    Returns:
        True if valid hex string matching expected length, False otherwise.
    """
    if not isinstance(tx_hash, str):
        return False

    clean_hash = tx_hash[2:] if tx_hash.startswith(("0x", "0X")) else tx_hash
    if len(clean_hash) != expected_length:
        return False

    try:
        int(clean_hash, 16)
        return True
    except ValueError:
        return False
