import re
from typing import Union

# Validation patterns for crypto addresses and keys
BTC_ADDRESS_PATTERN = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
ETH_ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_address(address: str, chain: str) -> bool:
    """Validates cryptocurrency addresses against chain-specific regex."""
    if chain.upper() == "BTC":
        return bool(BTC_ADDRESS_PATTERN.match(address))
    if chain.upper() == "ETH":
        return bool(ETH_ADDRESS_PATTERN.match(address))
    return False

def validate_checksum(data: str, expected_length: int = 64) -> bool:
    """Checks hex string format and length for hashes."""
    if not isinstance(data, str) or len(data) != expected_length:
        return False
    return all(c in "0123456789abcdefABCDEF" for c in data)

def sanitize_input(user_input: Union[str, int]) -> str:
    """Basic sanitization for crypto operation inputs."""
    return str(user_input).strip().lower()
