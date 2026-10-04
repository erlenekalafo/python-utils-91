import logging
import os
from logging.handlers import RotatingFileHandler

def setup_crypto_logger(name: str, log_file: str = "crypto_ops.log") -> logging.Logger:
    """Configures a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if function called multiple times
    if not logger.handlers:
        # 5MB per file, keep 3 backups
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
        
        # Optional: log to console as well
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Example usage for crypto modules
if __name__ == "__main__":
    crypto_logger = setup_crypto_logger("crypto_utils")
    crypto_logger.info("Logger initialized for blockchain validation")