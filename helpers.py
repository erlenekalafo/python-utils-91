import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Expects a valid JSON file path.
    """
    config = defaults.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        # In production crypto settings, failure to read config should be logged
        pass

    return config

def get_crypto_defaults() -> Dict[str, Any]:
    """
    Provides secure baseline defaults for crypto operations.
    """
    return {
        "network": "mainnet",
        "timeout": 30,
        "verify_ssl": True,
        "max_retries": 3
    }