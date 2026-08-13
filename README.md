# python-utils-91 

A collection of powerful and simple utilities designed to streamline cryptocurrency data management and analysis using Python. This library offers developers quick access to market data, price conversions, and wallet balances, making it an essential tool for anyone working in the crypto space.

## Features

- **Market Data Access**: Fetch real-time price data and historical market trends from popular cryptocurrency exchanges.
- **Currency Conversion**: Easily convert between different cryptocurrencies and fiat currencies with live rates.
- **Wallet Balance Tracking**: Monitor your crypto wallet balances across multiple blockchain networks with straightforward API calls.
- **Data Visualization Tools**: Generate insightful visualizations of market trends and portfolio performance using Matplotlib and Seaborn integration.

## Installation

To install the `python-utils-91` package, you can use pip by running the following command:

```bash
pip install python-utils-91
```

## Basic Usage Example

Here’s a simple example to get you started with fetching the latest Bitcoin price and converting it to Ethereum.

```python
from crypto_utils import CryptoUtils

# Initialize the utility class
utils = CryptoUtils()

# Get the latest Bitcoin price in USD
btc_price = utils.get_market_price('BTC', 'USD')
print(f"Current Bitcoin Price: ${btc_price}")

# Convert 1 Bitcoin to Ethereum
eth_value = utils.convert_currency('BTC', 'ETH', 1)
print(f"1 Bitcoin is worth {eth_value} Ethereum.")
```

With just a few lines of code, you can access critical cryptocurrency data and perform conversions seamlessly.

## License

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

Feel free to contribute and enhance the utility of this library in the ever-evolving crypto ecosystem!