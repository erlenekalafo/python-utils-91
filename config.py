import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of crypto application settings."""
    
    DEFAULTS = {
        "rpc_url": "https://mainnet.infura.io/v3/",
        "timeout": 30,
        "retry_attempts": 3,
        "log_level": "INFO"
    }

    def __init__(self, config_path: str = "config.json"):
        self.path = config_path
        self.config = self.DEFAULTS.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.config.copy()