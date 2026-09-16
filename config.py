import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "debug": False
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with system-wide defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {config_path}: {e}")
    
    # Override with environment variables if present
    env_mapping = {
        "RPC_URL": "rpc_url",
        "TIMEOUT": "timeout"
    }
    
    for env_var, key in env_mapping.items():
        value = os.getenv(env_var)
        if value is not None:
            # Attempt to cast numeric values from environment
            if value.isdigit():
                value = int(value)
            config[key] = value
            
    return config