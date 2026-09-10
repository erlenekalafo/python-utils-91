"""Constants for cryptocurrency data processing and validation."""

# Common cryptocurrency ticker symbols
SUPPORTED_COINS = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "USDT": "Tether",
    "SOL": "Solana",
    "ADA": "Cardano",
    "DOT": "Polkadot",
}

# Regular expressions for address validation
ADDRESS_REGEXES = {
    "BTC_LEGACY": "^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "BTC_BECH32": "^(bc1)[a-zA-HJ-NP-Z0-9]{25,39}$",
    "ETH": "^0x[a-fA-F0-9]{40}$",
}

# Decimals for standard tokens
TOKEN_DECIMALS = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6,
    "USDC": 6,
    "DAI": 18,
}

# Base API Endpoints for common data providers
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
BINANCE_BASE_URL = "https://api.binance.com/api/v3"


def get_decimals(ticker: str, default: int = 18) -> int:
    """Retrieve the standard decimal places for a given token ticker."""
    return TOKEN_DECIMALS.get(ticker.upper(), default)
