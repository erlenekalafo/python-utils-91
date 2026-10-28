import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'crypto.log', level: int = logging.INFO):
    """
    Configures a rotating file logger for cryptographic operations.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        # 5MB file rotation with 3 backup files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Optional console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Initialization for crypto modules
crypto_logger = setup_logger('crypto_utils')