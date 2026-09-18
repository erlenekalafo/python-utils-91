import hashlib
import hmac
import time
from typing import Any, Dict


class CryptoApiHandler:
    """Handles API request signing and webhook signature verification for crypto exchanges."""

    def __init__(self, api_key: str, api_secret: str) -> None:
        """Initializes the handler with API credentials."""
        self.api_key: str = api_key
        self.api_secret: bytes = api_secret.encode("utf-8")

    def sign_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Signs the payload dictionary by adding a timestamp and HMAC-SHA256 signature.

        Args:
            payload: The dictionary of request parameters to sign.

        Returns:
            A new dictionary containing the original params, timestamp, and signature.
        """
        signed_params = payload.copy()
        if "timestamp" not in signed_params:
            signed_params["timestamp"] = int(time.time() * 1000)

        query_string = "&".join(
            f"{key}={value}" for key, value in sorted(signed_params.items())
        )

        signature = hmac.new(
            self.api_secret, query_string.encode("utf-8"), hashlib.sha256
        ).hexdigest()

        signed_params["signature"] = signature
        return signed_params

    def verify_webhook_payload(self, payload: bytes, signature: str) -> bool:
        """Verifies an incoming webhook payload against a provided HMAC-SHA256 signature.

        Args:
            payload: The raw bytes received in the webhook request.
            signature: The signature header provided by the webhook sender.

        Returns:
            True if the signature is valid and matches, False otherwise.
        """
        expected_signature = hmac.new(
            self.api_secret, payload, hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(expected_signature, signature)
