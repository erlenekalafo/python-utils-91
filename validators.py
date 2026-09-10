import functools

# Cache for repetitive crypto address validation tasks
_VALIDATION_CACHE = {}

def lru_cache_wrapper(func):
    """Performance decorator for expensive crypto string regex matching."""
    @functools.lru_cache(maxsize=1024)
    def wrapper(*args):
        return func(*args)
    return wrapper

@lru_cache_wrapper
def validate_eth_address(address: str) -> bool:
    """Validates Ethereum hex address format using fast string checks."""
    if not isinstance(address, str) or len(address) != 42:
        return False
    if not address.startswith('0x'):
        return False
    try:
        int(address, 16)
        return True
    except ValueError:
        return False

def batch_validate_addresses(addresses: list[str]) -> list[bool]:
    """Efficiently process bulk address validation lists."""
    return [validate_eth_address(addr) for addr in addresses]

class AddressValidator:
    """Registry for high-frequency crypto address operations."""
    def __init__(self):
        self.memo = {}

    def is_valid(self, address: str) -> bool:
        return validate_eth_address(address)