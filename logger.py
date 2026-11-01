import logging
import sys
from datetime import datetime

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a standardized logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_transaction(logger: logging.Logger, tx_hash: str, status: str, amount: float):
    """Utility for standardized transaction audit logging."""
    timestamp = datetime.utcnow().isoformat()
    logger.info(f"[{timestamp}] TX: {tx_hash} | STATUS: {status} | AMT: {amount:.8f}")

def log_error(logger: logging.Logger, operation: str, error: Exception):
    """Formatted error reporting for crypto network failures."""
    logger.error(f"Operation '{operation}' failed: {str(error)}", exc_info=True)