import re

class InputValidationError(Exception):
    pass

def validate_address(address):
    if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
        raise InputValidationError("Invalid Ethereum address format.")

def validate_amount(amount):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise InputValidationError("Amount must be a positive number.")

def validate_transaction(address, amount):
    try:
        validate_address(address)
        validate_amount(amount)
    except InputValidationError as e:
        print(f'Input validation error: {e}')
        return False
    return True
