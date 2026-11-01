import os
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class NetworkConfig:
    """Configuration settings for a specific blockchain network."""
    name: str
    rpc_url: str
    chain_id: int
    timeout: float = 30.0
    headers: Dict[str, str] = field(default_factory=dict)

class CryptoConfig:
    """Global configuration manager for crypto utilities and RPC endpoints."""

    DEFAULT_NETWORKS: Dict[str, Dict[str, Any]] = {
        "ethereum": {
            "rpc_url": "https://mainnet.infura.io/v3/",
            "chain_id": 1,
        },
        "polygon": {
            "rpc_url": "https://polygon-rpc.com",
            "chain_id": 137,
        },
        "arbitrum": {
            "rpc_url": "https://arb1.arbitrum.io/rpc",
            "chain_id": 42161,
        },
    }

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Initialize configuration with optional API key override."""
        self.api_key: Optional[str] = api_key or os.getenv("CRYPTO_API_KEY")
        self._networks: Dict[str, NetworkConfig] = {}
        self._load_defaults()

    def _load_defaults(self) -> None:
        """Load default network configurations into internal storage."""
        for name, data in self.DEFAULT_NETWORKS.items():
            url: str = data["rpc_url"]
            if self.api_key and "infura.io" in url:
                url = f"{url}{self.api_key}"
            self._networks[name] = NetworkConfig(
                name=name,
                rpc_url=url,
                chain_id=int(data["chain_id"])
            )

    def get_network(self, name: str) -> NetworkConfig:
        """Retrieve network configuration by network name."""
        key = name.lower()
        if key not in self._networks:
            raise KeyError(f"Network '{name}' is not configured.")
        return self._networks[key]

    def register_network(self, config: NetworkConfig) -> None:
        """Register or overwrite a custom network configuration."""
        self._networks[config.name.lower()] = config
