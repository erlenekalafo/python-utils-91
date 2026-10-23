import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of crypto service configurations."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Updates internal config with JSON values from disk."""
        if not os.path.exists(filepath):
            return

        with open(filepath, 'r') as f:
            user_config = json.load(f)
            self._deep_update(self.config, user_config)

    def _deep_update(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        """Recursively merges update dict into base dict."""
        for key, value in update.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._deep_update(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves value by key with optional fallback."""
        return self.config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        """Returns the current full configuration mapping."""
        return self.config