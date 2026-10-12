from typing import Final, Dict, List

# Crypto network identifier mappings
NETWORK_IDS: Final[Dict[str, int]] = {
    "mainnet": 1,
    "testnet": 3,
    "sepolia": 11155111,
}

# Standard transaction fee limits in Gwei
MAX_GAS_LIMIT: Final[int] = 2000000
DEFAULT_GAS_PRICE: Final[float] = 20.0

# Supported cryptographic curves
SUPPORTED_CURVES: Final[List[str]] = ["secp256k1", "ed25519"]

# Protocol operational constants
API_TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3

def get_network_id(name: str) -> int:
    """Return the integer network ID for a given network name."""
    return NETWORK_IDS.get(name.lower(), 0)

def is_curve_supported(curve: str) -> bool:
    """Check if the provided cryptographic curve is currently enabled."""
    return curve in SUPPORTED_CURVES