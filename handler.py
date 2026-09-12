from typing import Dict, Any, Optional
import hashlib

class CryptoHandler:
    """Handles cryptographic signing and data validation operations."""

    def __init__(self, secret_key: str) -> None:
        """Initialize handler with a specific secret key."""
        self._secret_key: str = secret_key

    def generate_signature(self, payload: Dict[str, Any]) -> str:
        """Create SHA-256 hex signature from payload and secret."""
        message: str = f"{payload}{self._secret_key}"
        return hashlib.sha256(message.encode()).hexdigest()

    def validate_request(self, payload: Dict[str, Any], signature: str) -> bool:
        """Verify incoming request integrity against provided signature."""
        if not isinstance(payload, dict):
            return False
        
        expected: str = self.generate_signature(payload)
        return hashlib.compare_digest(expected, signature)

    def process_transaction(self, data: Dict[str, Any], sign: Optional[str] = None) -> Dict[str, Any]:
        """Process validated transaction and append status metadata."""
        is_valid: bool = False
        if sign:
            is_valid = self.validate_request(data, sign)

        return {
            "status": "success" if is_valid else "failed",
            "verified": is_valid,
            "payload_hash": hashlib.md5(str(data).encode()).hexdigest()
        }