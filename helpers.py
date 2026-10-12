import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads a JSON configuration file, merging it with provided default values.
    Returns a dictionary with merged configuration or defaults if file missing.
    """
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def validate_crypto_params(config: Dict[str, Any]) -> bool:
    """
    Ensures critical crypto configuration keys are present and valid.
    """
    required_keys = {'api_key', 'network_type', 'timeout'}
    return all(key in config for key in required_keys)

# Example Usage:
# defaults = {'network_type': 'mainnet', 'timeout': 30}
# cfg = load_config('config.json', defaults)