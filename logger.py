import logging
import sys
from typing import Optional

def get_crypto_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance for crypto operations.

    Args:
        name: The name of the logger instance.
        level: The logging severity level.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_trade_event(logger: logging.Logger, symbol: str, action: str, price: float) -> None:
    """
    Logs a specific cryptocurrency trade execution event.

    Args:
        logger: The logger instance to use.
        symbol: The currency pair ticker.
        action: Buy or Sell action.
        price: The execution price.
    """
    logger.info("trade execution: %s %s at %.8f", action.upper(), symbol, price)