import os
from typing import Dict, Any, Optional

class CryptoConfig:
    """Configuration manager for cryptocurrency API integrations and network settings.

    Supports loading configuration from environment variables with fallback defaults
    for mainnet and testnet environments.
    """

    def __init__(self, env: str = "production") -> None:
        """Initialize the crypto configuration manager.

        Args:
            env: The deployment environment, typically 'production' or 'development'.
        """
        self.env: str = env.lower()
        self.api_key: Optional[str] = os.getenv("CRYPTO_API_KEY")
        self.network: str = os.getenv("CRYPTO_NETWORK", "mainnet")
        self._endpoints: Dict[str, str] = {
            "mainnet": "https://api.mainnet.crypto-node.org/v1",
            "testnet": "https://api.testnet.crypto-node.org/v1"
        }

    def get_api_endpoint(self) -> str:
        """Retrieve the API endpoint corresponding to the selected network.

        Returns:
            The full URL path for the active node network.

        Raises:
            ValueError: If the configured network is unsupported.
        """
        endpoint = self._endpoints.get(self.network)
        if not endpoint:
            raise ValueError(f"Unsupported crypto network: {self.network}")
        return endpoint

    def get_auth_headers(self) -> Dict[str, str]:
        """Generate HTTP headers required for authenticating with the crypto API.

        Returns:
            A dictionary containing authorization and content-type headers.

        Raises:
            ValueError: If the API key environment variable is not configured.
        """
        if not self.api_key:
            raise ValueError("CRYPTO_API_KEY environment variable is not set")
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
