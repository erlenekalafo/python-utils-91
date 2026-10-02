import json
import os
from typing import Any, Dict, Optional

DEFAULT_CRYPTO_CONFIG: Dict[str, Any] = {
    "exchange": "binance",
    "base_currency": "USDT",
    "api_timeout_seconds": 30,
    "max_retries": 3,
    "enable_websocket": True,
    "rpc_nodes": {
        "ethereum": "https://mainnet.infura.io/v3/your_key",
        "polygon": "https://polygon-rpc.com",
    },
    "rate_limit_per_minute": 1200,
}

class ConfigLoader:
    """Loads and manages crypto application configuration with default fallback values."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CRYPTO_CONFIG.copy()
        if config_path:
            self.load_from_file(config_path)

    def load_from_file(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from a JSON file and updates default settings."""
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                    self._deep_update(self._config, user_config)
            except (json.JSONDecodeError, IOError) as err:
                raise RuntimeError(f"Failed to load config file {filepath}: {err}")
        return self._config

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a configuration value by key or fallback value."""
        return self._config.get(key, default)

    def _deep_update(self, base_dict: Dict[str, Any], update_dict: Dict[str, Any]) -> None:
        """Recursively merges user configuration into base configuration."""
        for key, value in update_dict.items():
            if isinstance(value, dict) and key in base_dict and isinstance(base_dict[key], dict):
                self._deep_update(base_dict[key], value)
            else:
                base_dict[key] = value

    @property
    def config(self) -> Dict[str, Any]:
        """Returns current loaded configuration dictionary."""
        return self._config
