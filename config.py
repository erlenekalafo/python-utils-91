import json
import os
from typing import Any, Dict

def load_crypto_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with provided fallback defaults.
    Supports crypto-specific environment overrides for API keys.
    """
    config = defaults.copy()

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Config loading failed: {e}. Using defaults.")

    # Override with env vars for sensitive credentials
    config['api_key'] = os.getenv('CRYPTO_API_KEY', config.get('api_key'))
    config['network_mode'] = os.getenv('NETWORK_MODE', config.get('network_mode', 'mainnet'))
    
    return config

if __name__ == '__main__':
    default_cfg = {
        'api_key': None,
        'retries': 3,
        'timeout': 30,
        'network_mode': 'testnet'
    }
    settings = load_crypto_config('config.json', default_cfg)
    print(f"Active config: {settings}")