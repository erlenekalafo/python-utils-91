import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging crypto configuration files."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Overrides defaults with values from a JSON file."""
        if not os.path.exists(filepath):
            return
            
        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Configuration error: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves config value by key."""
        return self.config.get(key, default)

# Default crypto constants
DEFAULT_SETTINGS = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def get_config(filepath: str = "config.json") -> ConfigLoader:
    """Factory function for global configuration access."""
    loader = ConfigLoader(DEFAULT_SETTINGS.copy())
    loader.load_from_file(filepath)
    return loader