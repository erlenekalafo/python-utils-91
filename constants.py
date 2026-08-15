CRYPTO_CURRENCIES = ['BTC', 'ETH', 'LTC', 'XRP']

API_URLS = {
    'coinmarketcap': 'https://api.coinmarketcap.com/v1/',
    'coingecko': 'https://api.coingecko.com/api/v3/',
}

DEFAULT_TIMEOUT = 10  # seconds

HEADER = {
    'User-Agent': 'python-utils-91 v1.0',
    'Accept': 'application/json',
}

CURRENCY_SYMBOLS = {
    'BTC': '₿',
    'ETH': 'Ξ',
    'LTC': 'Ł',
    'XRP': 'XRP',
}

# This is a mapping of currency pairs to their respective display names
CURRENCY_PAIRS = {
    'BTC/USD': 'Bitcoin to US Dollar',
    'ETH/USD': 'Ethereum to US Dollar',
    'LTC/USD': 'Litecoin to US Dollar',
    'XRP/USD': 'Ripple to US Dollar',
}

# Threshold values for trading strategies
PRICE_ALERT_THRESHOLD = 100  # USD
VOLUME_ALERT_THRESHOLD = 1000  # Number of coins

# Slippage percentage for trades
SLIPPAGE_PERCENTAGE = 1.5

# Dictionary for storing API keys or secrets for different exchanges
API_KEYS = {
    'binance': 'your_binance_api_key',
    'coinbase': 'your_coinbase_api_key',
}
