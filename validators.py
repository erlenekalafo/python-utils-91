import re
from typing import Union


def is_valid_eth_address(address: str) -> bool:
    """Check if the provided string is a valid Ethereum address."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_btc_address(address: str) -> bool:
    """Check if string is a valid Bitcoin address (Legacy, P2SH, Bech32)."""
    if not isinstance(address, str):
        return False
    btc_pattern = r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-0-9w-z]{38,59})$"
    return bool(re.match(btc_pattern, address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    """Validate 64-character hex transaction hash (optional 0x prefix)."""
    if not isinstance(tx_hash, str):
        return False
    clean_hash = tx_hash[2:] if tx_hash.startswith("0x") else tx_hash
    return bool(re.match(r"^[a-fA-F0-9]{64}$", clean_hash))


def normalize_address(address: str, chain: str = "eth") -> str:
    """Normalize address formatting based on target blockchain type."""
    if not isinstance(address, str):
        raise ValueError("Address must be a string")

    cleaned = address.strip()
    chain_lower = chain.lower()
    if chain_lower in ("eth", "ethereum"):
        if not is_valid_eth_address(cleaned):
            raise ValueError(f"Invalid Ethereum address: {cleaned}")
        return cleaned.lower()

    if chain_lower in ("btc", "bitcoin"):
        if not is_valid_btc_address(cleaned):
            raise ValueError(f"Invalid Bitcoin address: {cleaned}")
        return cleaned

    raise ValueError(f"Unsupported chain for normalization: {chain}")
