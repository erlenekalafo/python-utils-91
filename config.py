import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
    "debug": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load {filepath}: {e}. Using defaults.")
    
    return config

def get_network_settings() -> Dict[str, Any]:
    """Helper to fetch validated network configuration."""
    cfg = load_config()
    # Ensure critical settings are present
    return {
        "url": cfg.get("rpc_url"),
        "timeout": int(cfg.get("timeout", 30)),
        "retries": int(cfg.get("retries", 3))
    }