import logging
import sys
from typing import Optional

def setup_crypto_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures a standard logger for crypto utility modules.

    Args:
        name: The name of the logger instance.
        level: Logging severity level (default INFO).

    Returns:
        An initialized logging.Logger object.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

def log_trade_event(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Standardized formatting for blockchain and trading event logs.

    Args:
        logger: Active logging instance.
        message: The event description.
        level: Severity level (info, warning, or error).
    """
    levels: dict = {
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR
    }
    log_level: int = levels.get(level.lower(), logging.INFO)
    logger.log(log_level, f"[CRYPTO_TX] {message}")