import os
import json
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of crypto app configurations."""
    
    DEFAULTS = {
        "rpc_url": "https://mainnet.infura.io",
        "timeout": 30,
        "retries": 3,
        "verify_ssl": True
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = self.DEFAULTS.copy()
        self._load_file()

    def _load_file(self) -> None:
        """Load settings from JSON file if it exists."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        """Return the full configuration dictionary."""
        return self.settings