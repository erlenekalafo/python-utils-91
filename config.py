import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging crypto configuration settings."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Updates config dictionary from a local json file."""
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    user_config = json.load(f)
                    self.update_recursive(self.config, user_config)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Config loading failed: {e}")

    def update_recursive(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        """Deep update for nested configuration dictionaries."""
        for key, value in update.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self.update_recursive(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Access config values with optional fallback."""
        return self.config.get(key, default)

# Default configuration for crypto operations
DEFAULT_SETTINGS = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_strategy": "dynamic"
}

def get_config_loader() -> ConfigLoader:
    loader = ConfigLoader(DEFAULT_SETTINGS)
    if os.environ.get("CRYPTO_CONFIG_PATH"):
        loader.load_from_file(os.environ["CRYPTO_CONFIG_PATH"])
    return loader