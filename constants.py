from typing import Final, Dict

# Network identifiers for crypto protocols
MAINNET_ID: Final[int] = 1
TESTNET_ID: Final[int] = 2

# Standardized wallet address lengths
ETH_ADDR_LEN: Final[int] = 42
BTC_ADDR_LEN: Final[int] = 34

# Transaction status definitions
STATUS_PENDING: Final[str] = "pending"
STATUS_CONFIRMED: Final[str] = "confirmed"
STATUS_FAILED: Final[str] = "failed"

# Default protocol settings
DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

# Mapping for supported chain identifiers
CHAIN_MAP: Final[Dict[str, int]] = {
    "ethereum": MAINNET_ID,
    "bitcoin": MAINNET_ID,
    "sepolia": TESTNET_ID
}

def get_chain_id(chain_name: str) -> int:
    """Return the integer ID for a given blockchain name."""
    return CHAIN_MAP.get(chain_name.lower(), -1)

# Cryptographic operation constants
HASH_ALGORITHM: Final[str] = "sha256"
BLOCK_REWARD: Final[float] = 6.25