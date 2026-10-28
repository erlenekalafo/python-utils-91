import logging
import re
import sys
from typing import Optional

# Mask patterns for sensitive crypto data (e.g., private keys, API secrets)
PRIVATE_KEY_PATTERN = re.compile(r'(0x)?[a-fA-F0-9]{64}')
API_KEY_PATTERN = re.compile(r'(?i)(api[_-]?key|secret)["\\']?\s*[:=]\s*["\\']?([a-zA-Z0-9_\-]+)')

class CryptoMaskingFormatter(logging.Formatter):
    """Formatter that redacts private keys and secret tokens from log output."""
    
    def format(self, record: logging.LogRecord) -> str:
        original_msg = super().format(record)
        # Mask 64-character hex strings (potential private keys)
        masked_msg = PRIVATE_KEY_PATTERN.sub('[REDACTED_PRIVATE_KEY]', original_msg)
        # Mask API key values in log output
        masked_msg = API_KEY_PATTERN.sub(r'\1: [REDACTED_SECRET]', masked_msg)
        return masked_msg

def get_crypto_logger(
    name: str = "crypto_utils",
    level: int = logging.INFO,
    log_file: Optional[str] = None
) -> logging.Logger:
    """Configures and returns a specialized logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        formatter = CryptoMaskingFormatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            
    return logger