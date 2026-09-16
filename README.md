# python-utils-91

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python utility library designed to streamline common Web3 and cryptographic operations. It provides developers with robust tools for address validation, gas estimation, and secure key derivation across multiple EVM-compatible blockchains.

## Features

* **EVM Address Validation:** Fast, local checksum validation and format enforcement for Ethereum-compatible addresses.
* **BIP-39 HD Wallet Derivation:** Securely generate seed phrases and derive private/public keypairs using hierarchical deterministic paths.
* **Gas & Fee Estimation:** Fetch and format real-time optimal gas prices directly from mainnet RPC endpoints.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-91
```

## Quick Start

Validate an address and derive a keypair using the example below:

```python
from python_utils_91 import EVMValidator, KeyDeriver

# Validate an Ethereum address checksum
address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
if EVMValidator.is_valid_checksum(address):
    print("Address is valid!")

# Derive a private key from a BIP-39 mnemonic
mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
private_key = KeyDeriver.from_mnemonic(mnemonic, path="m/44'/60'/0'/0/0")
print(f"Derived Private Key: {private_key[:10]}...")
```

## License

This project is licensed under the MIT License.