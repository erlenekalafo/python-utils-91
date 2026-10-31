import os
from typing import Dict, Any, Optional

class CryptoConfig:
    """Configuration management for crypto operations."""

    def __init__(self, env: str = "prod") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "key_size": 2048,
            "algorithm": "RSA",
            "padding": "OAEP"
        }

    def get_setting(self, key: str) -> Optional[Any]:
        """Retrieve specific setting value by key."""
        return self.settings.get(key)

    def update_settings(self, new_settings: Dict[str, Any]) -> None:
        """Update multiple settings via dictionary input."""
        self.settings.update(new_settings)

def load_crypto_environment() -> Dict[str, str]:
    """Load environment-specific variables from system."""
    return {
        "NODE_URL": os.getenv("CRYPTO_NODE", "https://api.mainnet.io"),
        "API_KEY": os.getenv("CRYPTO_KEY", "default_key_val")
    }