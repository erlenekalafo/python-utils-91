import re

# Function to validate cryptocurrency addresses

def is_valid_address(address: str, currency: str) -> bool:
    """Validate the cryptocurrency address based on currency type."""
    patterns = {
        'bitcoin': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',
        'ethereum': r'^0x[a-fA-F0-9]{40}$',
        'litecoin': r'^[LM3][a-zA-Z0-9]{26,33}$'
    }

    pattern = patterns.get(currency.lower())
    if pattern:
        return re.match(pattern, address) is not None
    return False

# Function to validate transaction amount

def is_valid_amount(amount: float) -> bool:
    """Check if the transaction amount is valid (greater than zero)."""
    return amount > 0

# Example usage within a main processing loop

def process_transaction(address: str, currency: str, amount: float) -> None:
    if not is_valid_address(address, currency):
        raise ValueError('Invalid cryptocurrency address')
    if not is_valid_amount(amount):
        raise ValueError('Transaction amount must be greater than zero')

    # Proceed with transaction processing here
    print(f'Transacting {amount} {currency} to {address}')