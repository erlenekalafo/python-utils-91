import logging
import sys
from typing import Optional

def get_crypto_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a standardized logger for crypto utility modules."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

class CryptoLogger:
    """Helper class for tracking transactional events."""
    def __init__(self, name: str) -> None:
        self.logger = get_crypto_logger(name)

    def log_trade(self, symbol: str, amount: float, price: float) -> None:
        self.logger.info(f"Trade executed: {symbol} | Qty: {amount} | Price: {price}")

    def log_error(self, operation: str, error: Exception) -> None:
        self.logger.error(f"Failed {operation}: {str(error)}")