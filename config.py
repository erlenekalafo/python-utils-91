import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
    "api_key": None
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads crypto node configuration with sensible defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load {config_path}: {e}")
            
    return config

def get_required_key(config: Dict[str, Any], key: str) -> Any:
    """Validates existence of critical crypto configuration keys."""
    if key not in config or config[key] is None:
        raise ValueError(f"Missing required configuration: {key}")
    return config[key]