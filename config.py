import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth.llamarpc.com",
    "timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.2,
    "enable_cache": True,
}


class ConfigLoader:
    """Loads application configuration with fallback defaults for crypto utilities."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from file and environment variables."""
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        self._config.update(file_data)
            except (json.JSONDecodeError, IOError) as err:
                print(f"Warning: Failed to load config file ({err}). Using defaults.")

        # Environment variable overrides (e.g. CRYPTO_RPC_URL)
        env_mappings = {
            "CRYPTO_NETWORK": "network",
            "CRYPTO_RPC_URL": "rpc_url",
            "CRYPTO_TIMEOUT": "timeout",
        }
        for env_var, config_key in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                if config_key == "timeout":
                    try:
                        self._config[config_key] = int(val)
                    except ValueError:
                        pass
                else:
                    self._config[config_key] = val

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        """Returns read-only view of current configuration."""
        return self._config.copy()
