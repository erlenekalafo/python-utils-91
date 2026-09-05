# python-utils-91

A high-performance Python toolkit designed for cryptocurrency data analysis, automated trade execution, and wallet management. This library simplifies complex blockchain interactions, allowing developers to build robust trading bots and portfolio trackers with minimal boilerplate.

## Features

*   **Real-time Price Aggregator:** Efficiently fetch live ticker data from major exchanges (Binance, Kraken, Coinbase) using asynchronous requests.
*   **Encrypted Wallet Utilities:** Securely generate, import, and manage mnemonic phrases and private keys with industry-standard AES-256 encryption.
*   **Advanced Order Engine:** A lightweight wrapper for executing limit and market orders with built-in slippage protection and rate-limit handling.
*   **Portfolio Snapshotter:** Generate instant, human-readable reports on asset allocation and historical ROI across multiple hot and cold wallets.

## Installation

Ensure you have Python 3.8+ installed. Install the package via pip:

```bash
pip install python-utils-91
```

For development mode and access to experimental trading modules:

```bash
git clone https://github.com/Developer/python-utils-91.git
cd python-utils-91
pip install -r requirements.txt
```

## Basic Usage

Quickly fetch current BTC/USDT price data from the Binance API module:

```python
from pyutils_91.exchange import ExchangeClient

# Initialize client
client = ExchangeClient(api_key="YOUR_KEY", api_secret="YOUR_SECRET")

# Fetch ticker and print market data
ticker = client.get_ticker(symbol="BTC/USDT")
print(f"Current Price: {ticker['last_price']}")

# Place a market buy order
order = client.create_order(symbol="BTC/USDT", side="buy", amount=0.01)
print(f"Order Status: {order['status']}")
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.