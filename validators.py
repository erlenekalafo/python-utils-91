import re

# Common regex patterns for standard crypto formats
ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_REGEX = re.compile(r"^(1|3|[bc1q])[a-zA-HJ-NP-Z0-9]{25,59}$")
SHA256_REGEX = re.compile(r"^[a-fA-F0-9]{64}$")

def validate_ethereum_address(address: str) -> bool:
    """
    Validate if a given string matches the Ethereum address format.

    Checks for the standard '0x' prefix followed by 40 hexadecimal characters.
    Note: This validates structural format, not EIP-55 checksum validation.

    Args:
        address: The string representation of the Ethereum address.

    Returns:
        True if the format is valid, False otherwise.
    """
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_REGEX.match(address))

def validate_bitcoin_address(address: str) -> bool:
    """
    Validate if a given string matches standard Bitcoin address formats.

    Supports legacy (1...), Pay-to-Script-Hash (3...), and Bech32/SegWit (bc1...) prefixes.

    Args:
        address: The string representation of the Bitcoin address.

    Returns:
        True if the format matches standard Bitcoin address prefixes and length, False otherwise.
    """\