import re

class CryptoValidator:
    """Utility to validate crypto-specific input formats."""

    @staticmethod
    def is_valid_address(address: str) -> bool:
        """Checks if string follows standard 0x hex address format."""
        if not isinstance(address, str):
            return False
        pattern = r'^0x[a-fA-F0-9]{40}$'
        return bool(re.match(pattern, address))

    @staticmethod
    def is_valid_amount(amount: str) -> bool:
        """Checks if amount is a positive numeric string."""
        try:
            val = float(amount)
            return val > 0
        except (ValueError, TypeError):
            return False

def validate_transaction_data(data: dict) -> bool:
    """Comprehensive validation for incoming processing tasks."""
    required_fields = ['address', 'amount', 'currency']
    
    if not all(k in data for k in required_fields):
        return False
    
    if not CryptoValidator.is_valid_address(data['address']):
        return False
        
    if not CryptoValidator.is_valid_amount(data['amount']):
        return False
        
    return True