import logging
from logging.handlers import RotatingFileHandler
import os

def setup_rotating_logger(
    name: str = "python_utils_91",
    log_file: str = "crypto_utils.log",
    max_bytes: int = 10485760,  # 10 MB
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """Set up a logger with rotating file handler and console output."""
    logger = logging.getLogger(name)
    # Prevent adding handlers multiple times
    if not logger.handlers:
        logger.setLevel(level)
        # Ensure directory for log file
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # Rotating file handler
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setLevel(level)
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        # Formatter with timestamp, level, name and message
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger

# Usage example to demonstrate it works
if __name__ == "__main__":
    logger = setup_rotating_logger()
    logger.info("Logger setup complete with rotation enabled")
    logger.debug("This debug message may not appear based on level")
    logger.warning("Sample warning for testing rotation")
