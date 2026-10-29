# python-utils-91

`python-utils-91` is a robust collection of Python modules designed to streamline cryptocurrency data acquisition and wallet management. It provides high-performance utilities for interacting with exchange APIs and executing secure blockchain transactions with minimal latency.

### Features

*   **Real-time Price Aggregator:** Efficiently fetch live ticker data from multiple major exchanges (Binance, Coinbase, Kraken) using asynchronous requests.
*   **Wallet Address Validator:** Built-in checksum validation and format verification for BTC, ETH, and SOL wallet addresses to prevent transaction errors.
*   **Encrypted Key Manager:** Securely store and load API credentials using AES-256 encryption, ensuring your private keys remain protected at rest.
*   **Transaction Hash Tracker:** Lightweight monitor to track and verify the confirmation status of blockchain transactions via public RPC nodes.

### Installation

Ensure you have Python 3.8+ installed. Install the package directly via pip:

```bash
pip install python-utils-91
```

To install from source for development purposes:

```bash
git clone https://github.com/Developer/python-utils-91.git
cd python-utils-91
pip install -r requirements.txt
```

### Usage

Here is a quick example of how to fetch the current BTC/USDT price from Binance:

```python
from crypto_utils import PriceFetcher

# Initialize the fetcher
fetcher = PriceFetcher()

# Get the latest ticker price
price = fetcher.get_price("BTC", "USDT", exchange="binance")

print(f"Current BTC Price: {price} USDT")
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.