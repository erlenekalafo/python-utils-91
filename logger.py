import logging
import sys

def get_crypto_logger(name: str) -> logging.Logger:
    """Initializes a standard logger for crypto operations."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def log_transaction(logger: logging.Logger, tx_id: str, status: str) -> None:
    """Helper to standardize transaction status logging."""
    logger.info(f"Transaction {tx_id} status updated to: {status}")

def log_error(logger: logging.Logger, operation: str, error: Exception) -> None:
    """Helper for uniform error reporting in crypto modules."""
    logger.error(f"Critical failure during {operation}: {str(error)}")