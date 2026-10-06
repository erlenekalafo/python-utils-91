import re
from typing import Any

def validate_ethereum_address(address: Any) -> bool:
    """
    Validates an Ethereum address structure.
    Handles edge cases like wrong types, incorrect length, and hex format.
    """
    if not isinstance(address, str):
        return False

    # Normalize and handle optional prefix
    addr_clean = address[2:] if address.lower().startswith("0x") else address

    # Check exact hex length (40 hex characters = 20 bytes)
    if len(addr_clean) != 40:
        return False

    # Safe hex parsing to avoid conversion exceptions
    try:
        int(addr_clean, 16)
    except ValueError:
        return False

    return True

def validate_bitcoin_address(address: Any) -> bool:
    """
    Performs safety and format checks on legacy (1, 3) and Bech32 (bc1) BTC addresses.
    Handles whitespace, invalid characters, and structure anomalies.
    """
    if not isinstance(address, str):
        return False

    address = address.strip()
    if not address:
        return False

    # Legacy addresses (Base58check without 'O', 'I', 'l', '0')
    if address.startswith(("1", "3")):
        if any(char in address for char in "OI0l"):
            return False
        return 26 <= len(address) <= 35

    # Bech32 addresses (SegWit)
    elif address.lower().startswith("bc1"):
        bech32_chars = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
        parts = address.lower().split("1")
        if len(parts) < 2 or parts[0] != "bc":
            return False
        data_part = parts[-1]
        return len(data_part) >= 6 and all(char in bech32_chars for char in data_part)

    return False

def validate_crypto_hash(tx_hash: Any, byte_length: int = 32) -> bool:
    """
    Validates a transaction or block hash structure (typically 32 bytes/64 hex characters).
    Catches empty values, abnormal prefixes, and length mismatches.
    """
    if not isinstance(tx_hash, str):
        return False

    clean_hash = tx_hash[2:] if tx_hash.lower().startswith("0x") else tx_hash
    expected_len = byte_length * 2

    if len(clean_hash) != expected_len:
        return False

    return bool(re.fullmatch(r"[0-9a-fA-F]+", clean_hash))
