import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_limit": 21000
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Retrieves specific setting from loaded configuration."""
    config = load_config()
    return config.get(key, default)