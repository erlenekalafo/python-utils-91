import os
import json
from typing import Dict, Any, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "default_exchange": "binance",
    "base_currency": "USD",
    "timeout_seconds": 30,
    "max_retries": 3,
    "rate_limit_calls": 100,
    "rate_limit_period": 60,
    "endpoints": {
        "binance": "https://api.binance.com/api/v3",
        "kraken": "https://api.kraken.com/0/public",
        "coinbase": "https://api.exchange.coinbase.com"
    },
    "gas_limit_buffer": 1.2,
    "enable_logging": True
}

class ConfigLoader:
    """Loads and manages configuration settings with crypto defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Load configuration from file if provided and merge with env vars."""
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self._update_nested_dict(self._config, file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config file: {err}")

        self._override_from_env()
        return self._config

    def _update_nested_dict(self, target: dict, source: dict) -> None:
        """Recursively update target dictionary with source dictionary."""
        for key, value in source.items():
            if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                self._update_nested_dict(target[key], value)
            else:
                target[key] = value

    def _override_from_env(self) -> None:
        """Override configuration options using CRYPTO_ prefixed env variables."""
        if exchange := os.getenv("CRYPTO_DEFAULT_EXCHANGE"):
            self._config["default_exchange"] = exchange
        if timeout := os.getenv("CRYPTO_TIMEOUT"):
            try:
                self._config["timeout_seconds"] = int(timeout)
            except ValueError:
                pass

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration parameter by key."""
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        """Return full current configuration dict."""
        return self._config