import logging
from typing import Dict, Any, Optional

# Configure logging for crypto operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('crypto_handler')

class CryptoHandler:
    """Handles cryptographic payload processing and validation."""

    def __init__(self, key_id: str):
        self.key_id = key_id
        self.is_active = True

    def process_payload(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Sanitizes and prepares payload for encryption routines."""
        if not data or 'signature' not in data:
            logger.error('Invalid payload structure received')
            return None

        try:
            sanitized = {
                'id': data.get('id', 'unknown'),
                'payload': data['payload'],
                'timestamp': data.get('ts', 0)
            }
            return sanitized
        except KeyError as e:
            logger.warning(f'Missing required field: {e}')
            return None

    def reset_session(self) -> None:
        """Reinitializes handler state."""
        self.is_active = False
        logger.info(f'Session {self.key_id} reset successfully')
        self.is_active = True

def get_handler(key_id: str) -> CryptoHandler:
    """Factory function for creating clean handler instances."""
    return CryptoHandler(key_id=key_id)