import os
from typing import Dict, Any

class CryptoConfig:
    """Configuration management for crypto operations."""
    
    def __init__(self, env: str = "production") -> None:
        self.env = env
        self.settings: Dict[str, Any] = {
            "production": {
                "max_retries": 5,
                "timeout": 30,
                "fee_multiplier": 1.05
            },
            "development": {
                "max_retries": 1,
                "timeout": 10,
                "fee_multiplier": 1.0
            }
        }

    def get_setting(self, key: str) -> Any:
        """Retrieve specific setting based on environment."""
        return self.settings.get(self.env, {}).get(key)

    @classmethod
    def from_env(cls) -> 'CryptoConfig':
        """Initialize config from system environment variables."""
        env = os.getenv("APP_ENV", "production")
        return cls(env)

def get_default_config() -> CryptoConfig:
    """Factory function for global config instance."""
    return CryptoConfig.from_env()