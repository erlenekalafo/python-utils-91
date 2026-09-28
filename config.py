import os
import json
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of crypto app configurations."""

    DEFAULT_CONFIG = {
        "rpc_url": "https://mainnet.infura.io/v3/",
        "timeout": 30,
        "retry_attempts": 3,
        "log_level": "INFO"
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """Loads config from file, merging with defaults."""
        config = self.DEFAULT_CONFIG.copy()

        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass
        
        # Override with environment variables if present
        for key in config:
            env_val = os.getenv(f"CRYPTO_{key.upper()}")
            if env_val:
                # Attempt integer conversion for numerical fields
                try:
                    config[key] = int(env_val)
                except ValueError:
                    config[key] = env_val
        
        return config