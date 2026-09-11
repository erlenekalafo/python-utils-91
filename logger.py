import logging
import sys
from typing import Optional

class CryptoLogger:
    """Standardized logger for crypto-related operations."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational crypto events."""
        self.logger.info(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """Log critical trading or network errors."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Log non-critical warnings like rate limits."""
        self.logger.warning(message)

def get_logger(name: str, level: Optional[int] = None) -> CryptoLogger:
    """Factory function to retrieve a crypto logger instance."""
    return CryptoLogger(name, level or logging.INFO)