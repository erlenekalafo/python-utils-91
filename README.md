[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-91

A lightweight, high-performance Python utility suite designed to streamline blockchain interactions, wallet validation, and gas fee estimation across EVM-compatible networks. This library provides developers with highly optimized, production-ready cryptographic helpers to accelerate the development of decentralized applications, MEV bots, and Web3 integrations.

## Features

- **Multi-Chain Address Validation:** Out-of-the-box checksum validation for EVM, Solana, and Bitcoin (Bech32) addresses.
- **Optimized Gas Estimation:** Fast, real-time gas fee suggestions leveraging public decentralized RPC endpoints.
- **Ultra-Lightweight ABI Encoder:** Encode and decode smart contract transactions without importing heavy dependencies like `web3.py`.
- **Mnemonic & Key Generation:** Secure, BIP-39 compliant seed phrase generation and private key derivation.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-91
```

## Quick Start

Validate an Ethereum address and fetch real-time optimal gas prices with just a few lines of code:

```python
from python_utils_91 import EVMAddress, GasEstimator

# Validate Ethereum checksum address
address = "0x71C7656EC7ab88b098defB751B7401B5f6d1476B"
if EVMAddress.is_valid(address):
    print(f"Address {address} is valid.")

# Fetch optimal gas fees for Ethereum Mainnet
estimator = GasEstimator(chain_id=1)
gas_prices = estimator.get_suggested_fees()

print(f"Standard Gas: {gas_prices.standard} Gwei")
print(f"Fast Gas: {gas_prices.fast} Gwei")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.