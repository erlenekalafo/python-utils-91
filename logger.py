import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='crypto_logger', log_file='app.log', level=logging.INFO):
    """
    Configures a rotating file logger for crypto operations.
    Max size: 5MB per file, keeps 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # 5MB = 5 * 1024 * 1024 bytes
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5242880, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Optional: Log to console as well
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

if __name__ == "__main__":
    log = setup_logger()
    log.info("Logger initialization successful")