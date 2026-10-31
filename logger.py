import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


class CryptoLogFormatter(logging.Formatter):
    """Custom log formatter providing readable context for crypto operations."""

    DEFAULT_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    def __init__(self, fmt: Optional[str] = None):
        super().__init__(fmt=fmt or self.DEFAULT_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")


def setup_crypto_logger(
    name: str = "crypto_utils",
    log_file: str = "logs/crypto_bot.log",
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures a logger with standard stdout and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent attaching duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    formatter = CryptoLogFormatter()

    # Console stream handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Log file rotation handler
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            filename=log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log_trade_event(logger: logging.Logger, symbol: str, side: str, price: float, amount: float) -> None:
    """Helper to log trade execution details in a consistent format."""
    logger.info(f"TRADE EXECUTION | {side.upper()} {amount:.4f} {symbol} @ {price:.8f}")
