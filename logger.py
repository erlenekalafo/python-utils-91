import logging
from logging.handlers import RotatingFileHandler
import os

def setup_crypto_logger(name: str, log_file: str = 'crypto.log') -> logging.Logger:
    """Configures a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if function called multiple times
    if not logger.handlers:
        # 5MB per file, keep 5 historical backups
        handler = RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=5
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Optional stream handler for console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Instance for project-wide use
logger = setup_crypto_logger('python-utils-91')