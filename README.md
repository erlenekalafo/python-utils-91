# python-utils-91

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A collection of Python utilities for cryptocurrency development and data handling. It offers lightweight, dependency-minimal tools for fetching market data, validating addresses, and performing common blockchain calculations.

## Features
- Retrieve real-time and historical prices for over 100 cryptocurrencies through CoinGecko and Binance
- Validate wallet addresses for Bitcoin, Ethereum, Solana, and several other networks
- Estimate transaction fees and gas costs on Ethereum and EVM-compatible chains
- Convert between base units (satoshis, wei, lamports) and standard denominations

## Installation

```bash
pip install python-utils-91
```

From source:

```bash
git clone https://github.com/Developer/python-utils-91.git
cd python-utils-91
pip install -e .
```

## Usage

```python
from python_utils_91 import prices, addresses

# Fetch current price
btc_price = prices.get_price("bitcoin", "usd")

# Validate an address
is_valid = addresses.is_valid("bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", "bitcoin")
```