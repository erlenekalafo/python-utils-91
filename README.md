# python-utils-91

A high-performance toolkit for crypto developers designed to streamline wallet management, block exploration, and transaction signing. This library provides lightweight abstractions to interact with EVM-compatible chains without the overhead of heavy full-node dependencies.

### Features

*   **Secure Key Handling:** Built-in utilities for BIP-39 mnemonic generation and deterministic private key derivation using industry-standard elliptic curve cryptography.
*   **Gas Estimation Engine:** Real-time fee calculation logic that analyzes pending mempool traffic to optimize transaction speed and cost.
*   **ABI Decoding:** Seamless translation of low-level contract interaction data into human-readable Python dictionaries.
*   **Asynchronous RPC Requests:** Fully non-blocking WebSocket and HTTP providers for high-frequency data streaming and event listening.

### Installation

Install the package via pip:

```bash
pip install python-utils-91
```

For development builds, clone the repository and install the requirements:

```bash
git clone https://github.com/Developer/python-utils-91.git
cd python-utils-91
pip install -r requirements.txt
```

### Basic Usage

Quickly fetch the current balance of an address on the Ethereum mainnet:

```python
from python_utils_91 import CryptoClient

# Initialize the client with an RPC endpoint
client = CryptoClient(rpc_url="https://eth.llamarpc.com")

# Retrieve balance in Wei
balance = client.get_balance("0x742d35Cc6634C0532925a3b844Bc454e4438f44e")
print(f"Address Balance: {client.to_ether(balance)} ETH")
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.