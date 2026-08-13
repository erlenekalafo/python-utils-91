import re

# Validate an email address using regex

def is_valid_email(email: str) -> bool:
    """Check if the email format is valid."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Validate a cryptocurrency address (example for Bitcoin)

def is_valid_btc_address(address: str) -> bool:
    """Check if the Bitcoin address format is valid."""
    if len(address) < 26 or len(address) > 35:
        return False
    # Basic regex for Bitcoin address
    btc_regex = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
    return re.match(btc_regex, address) is not None

# Validate if a string is a numeric value

def is_numeric(value: str) -> bool:
    """Check if the value is numeric."""
    try:
        float(value)
        return True
    except ValueError:
        return False

# Validate if a string is a hex color code

def is_valid_hex_color(color: str) -> bool:
    """Check if the string is a valid hex color code."""
    hex_color_regex = r'^#[0-9a-fA-F]{6}$'
    return re.match(hex_color_regex, color) is not None
