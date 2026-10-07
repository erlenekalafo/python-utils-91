# python-utils-91

`python-utils-91` is a robust toolkit designed to streamline interactions with cryptocurrency exchanges and blockchain data. It provides high-performance wrappers for market data retrieval, wallet balance monitoring, and secure signing operations.

## Features

*   **Exchange Aggregator:** Unified asynchronous client for fetching real-time order books and ticker data across multiple major CEX APIs.
*   **Wallet Auditor:** Automated script to track ERC-20 token balances and detect suspicious outgoing transactions.
*   **Secure Signing Module:** Lightweight helper functions for EIP-712 typed data signing using standard Python cryptographic libraries.
*   **Rate-Limit Management:** Intelligent request queuing to handle exchange-specific API throttling without dropped connections.

## Installation

Ensure you have Python 3.9+ installed. Install the package via pip:

```bash
pip install python-utils-91
```

For development dependencies, clone the repository and run:

```bash
git clone https://github.com/Developer/python-utils-91.git
cd python-utils-91
pip install -r requirements.txt
```

## Basic Usage

Quickly fetch the latest ticker price for a trading pair from supported exchanges:

```python
from crypto_utils import ExchangeClient

# Initialize client for Binance
client = ExchangeClient(exchange='binance')

# Get BTC/USDT ticker
price = client.get_ticker('BTC/USDT')
print(f"Current BTC Price: {price['last']}")

# Async fetch historical data
history = await client.get_ohlcv('ETH/USDT', timeframe='1h')
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.