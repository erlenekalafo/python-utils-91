import os
from typing import Dict, Any, Optional

class CryptoConfig:
    """Configuration manager for cryptographic parameters."""

    def __init__(self, env: str = "production") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "key_size": 2048,
            "algorithm": "RSA",
            "padding": "OAEP"
        }

    def get_setting(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a specific setting with a fallback."""
        return self.settings.get(key, default)

    def update_settings(self, new_settings: Dict[str, Any]) -> None:
        """Update existing configuration with a dictionary."""
        self.settings.update(new_settings)

    @property
    def is_production(self) -> bool:
        """Check if current environment is production."""
        return self.env == "production"

    def __repr__(self) -> str:
        """Return string representation of configuration."""
        return f"CryptoConfig(env={self.env}, settings={self.settings})"