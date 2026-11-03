import logging
import sys
from typing import Optional

class CryptoLogger:
    """Centralized logger for crypto transaction monitoring."""
    def __init__(self, name: str = "crypto-utils"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, operation: str, error: Exception, context: Optional[dict] = None) -> None:
        """Handles edge case logging with safe context extraction."""
        try:
            error_type = type(error).__name__
            details = f"Context: {context}" if context else "No context provided"
            
            if isinstance(error, (ValueError, TypeError, KeyError)):
                self.logger.error(f"Invalid input during {operation}: {error_type} - {error} | {details}")
            elif isinstance(error, ConnectionError):
                self.logger.critical(f"Network failure during {operation}: {error} | Check RPC connectivity")
            else:
                self.logger.exception(f"Unexpected runtime error during {operation}: {error}")
        except Exception as e:
            # Fallback to prevent logging loop if stream is corrupted
            print(f"Critical logging failure: {e}", file=sys.stderr)

logger = CryptoLogger()