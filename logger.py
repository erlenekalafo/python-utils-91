import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'crypto_app', log_file: str = 'crypto.log', level=logging.INFO):
    """Initializes a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        # File rotation: 5MB max per file, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Optional stream output for console visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Global instance for project-wide use
crypto_logger = setup_logger()