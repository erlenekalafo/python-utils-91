"""Cryptographic address and hash validation utilities."""

import re
from typing import Optional


def is_valid_btc_address(address: str) -> bool:
    """Validate Bitcoin mainnet address format (Legacy, Nested SegWit, Native SegWit).

    Args:
        address: The Bitcoin address string to validate.

    Returns:
        True if the address matches standard Bitcoin formats, False otherwise.
    """
    if not address or not isinstance(address, str):
        return False
    pattern = r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-0-939-z]{8,87})$"
    return bool(re.match(pattern, address))


def is_valid_eth_address(address: str) -> bool:
    """Validate Ethereum public address format.

    Args:
        address: The hex string representation of an Ethereum address.

    Returns:
        True if the address is a valid 40-character hex string prefixed with 0x.
    """
    if not address or not isinstance(address, str):
        return False
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))


def is_valid_tx_hash(tx_hash: str, expected_length: int = 64) -> bool:
    """Validate standard hexadecimal transaction hash format.

    Args:
        tx_hash: The transaction hash string to check.
        expected_length: Expected length of hex characters (default 64 for SHA-256).

    Returns:
        True if valid hex of correct length, False otherwise.
    """
    if not tx_hash or not isinstance(tx_hash, str):
        return False
    clean_hash = tx_hash.lower().replace("0x", "")
    if len(clean_hash) != expected_length:
        return False
    return all(c in "0123456789abcdef" for c in clean_hash)


def sanitize_wallet_address(address: Optional[str]) -> Optional[str]:
    """Strip surrounding whitespaces and normalize wallet address string.

    Args:
        address: Raw input wallet address or None.

    Returns:
        Trimmed wallet address, or None if input is empty or invalid.
    """
    if not address:
        return None
    cleaned = address.strip()
    return cleaned if len(cleaned) > 0 else None
