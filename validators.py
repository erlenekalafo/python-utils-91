import re
import logging

# Configure basic logging for crypto operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('crypto-utils')

class InputValidator:
    """Utility class for validating crypto-related inputs."""

    @staticmethod
    def is_valid_address(address: str) -> bool:
        """Validates standard hex-based crypto wallet addresses."""
        if not isinstance(address, str) or not address.startswith('0x'):
            return False
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        """Ensures transaction amounts are positive numbers."""
        return isinstance(amount, (int, float)) and amount > 0

def process_transaction(data: dict):
    """Main loop entry point with input validation."""
    address = data.get('address')
    amount = data.get('amount')

    if not InputValidator.is_valid_address(address):
        logger.error(f"Invalid address format: {address}")
        return False

    if not InputValidator.is_valid_amount(amount):
        logger.error(f"Invalid transaction amount: {amount}")
        return False

    logger.info(f"Processing secure transaction for {address}")
    return True

if __name__ == "__main__":
    # Example usage for test coverage
    sample = {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': 0.05}
    process_transaction(sample)