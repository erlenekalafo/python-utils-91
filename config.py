import os
import json
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "exchange": "binance",
    "api_key": "",
    "api_secret": "",
    "use_testnet": True,
    "base_url": "https://testnet.binance.vision",
    "timeout_seconds": 30,
    "max_retries": 3,
    "default_symbol": "BTC/USDT",
    "slippage_tolerance": 0.005,
}


class ConfigLoader:
    """Loads and merges crypto trading configuration with fallback defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else None
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def _load_from_file(self) -> Dict[str, Any]:
        if not self.config_path or not self.config_path.exists():
            return {}
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as err:
            raise ValueError(f"Failed to parse configuration file: {err}")

    def _load_from_env(self) -> Dict[str, Any]:
        env_mappings = {
            "CRYPTO_EXCHANGE": "exchange",
            "CRYPTO_API_KEY": "api_key",
            "CRYPTO_API_SECRET": "api_secret",
            "CRYPTO_USE_TESTNET": "use_testnet",
            "CRYPTO_DEFAULT_SYMBOL": "default_symbol",
        }
        env_config: Dict[str, Any] = {}
        for env_key, config_key in env_mappings.items():
            val = os.getenv(env_key)
            if val is not None:
                if config_key == "use_testnet":
                    val = val.lower() in ("true", "1", "yes")
                env_config[config_key] = val
        return env_config

    def load(self) -> Dict[str, Any]:
        """Merges defaults, file settings, and environment variables."""
        file_config = self._load_from_file()
        env_config = self._load_from_env()

        self.config.update(file_config)
        self.config.update(env_config)
        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a specific configuration parameter."""
        return self.config.get(key, default)
