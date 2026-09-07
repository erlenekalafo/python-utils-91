import re
import hashlib

class CryptoDataHandler:
    """Utility class for validating and formatting cryptocurrency data."""

    ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")

    @classmethod
    def validate_ethereum_address(cls, address: str) -> bool:
        """
        Validates if the given string is a valid Ethereum address.
        Supports standard hex format and basic checksum structure check.
        """
        if not isinstance(address, str):
            return False
        return bool(cls.ETH_ADDRESS_PATTERN.match(address))

    @classmethod
    def generate_sha256_hash(cls, data: bytes) -> str:
        """Generates a SHA-256 hash string for the given raw bytes data."""
        if not isinstance(data, bytes):
            raise TypeError("Data must be of bytes type")
        return hashlib.sha256(data).hexdigest()

    @classmethod
    def format_transaction_payload(cls, sender: str, recipient: str, amount_wei: int, nonce: int) -> dict:
        """
        Formats a standard transaction payload after validating basic parameters.
        """
        if not cls.validate_ethereum_address(sender) or not cls.validate_ethereum_address(recipient):
            raise ValueError("Invalid sender or recipient Ethereum address")
        
        if amount_wei < 0 or nonce < 0:
            raise ValueError("Amount and nonce must be non-negative integers")

        return {
            "from": sender.lower(),
            "to": recipient.lower(),
            "value": hex(amount_wei),
            "nonce": nonce,
            "gasLimit": hex(21000)
        }