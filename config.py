import os
import json
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of crypto app settings."""
    
    def __init__(self, defaults: Dict[str, Any]):
        self.config = defaults

    def load_from_env(self, prefix: str = "CRYPTO_") -> None:
        """Overrides defaults with environment variables."""
        for key in self.config.keys():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                self.config[key] = os.environ[env_key]

    def load_from_json(self, filepath: str) -> None:
        """Updates config with values from a JSON file."""
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                self.config.update(file_data)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves value safely from internal config."""
        return self.config.get(key, default)

def get_default_config() -> Dict[str, Any]:
    return {
        "api_key": "",
        "network": "mainnet",
        "timeout": 30,
        "db_path": "./data/crypto.db"
    }

# Usage example
if __name__ == "__main__":
    loader = ConfigLoader(get_default_config())
    loader.load_from_env()
    print(f"Active network: {loader.get('network')}")