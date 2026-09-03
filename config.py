import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading configuration with fallback defaults."""
    
    DEFAULT_CONFIG = {
        "network": "mainnet",
        "timeout": 30,
        "retry_attempts": 3,
        "log_level": "INFO"
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Reads JSON file and merges with internal defaults."""
        if not os.path.exists(self.config_path):
            return self.DEFAULT_CONFIG
        
        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                return {**self.DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        """Access configuration values safely."""
        return self.config.get(key, default)

    def get_int(self, key: str) -> int:
        """Force integer return type for numeric settings."""
        return int(self.config.get(key, 0))