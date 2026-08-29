import logging
import os
import sys
from logging.handlers import RotatingFileHandler

class CryptoLogger:
    """Logger for crypto utilities with organized handlers and rotation."""

    def __init__(self, name="crypto_utils", log_file="crypto_operations.log", max_bytes=10485760, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # clear existing handlers to prevent duplicates after reorganization
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        # console for real-time monitoring
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        # rotating file handler for automatic cleanup of old logs
        os.makedirs("logs", exist_ok=True)
        log_path = os.path.join("logs", log_file)
        file_handler = RotatingFileHandler(
            log_path, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_format)
        self.logger.addHandler(file_handler)

    def log_info(self, message, **kwargs):
        self.logger.info(message, extra=kwargs)

    def log_warning(self, message, **kwargs):
        self.logger.warning(message, extra=kwargs)

    def log_error(self, message, **kwargs):
        self.logger.error(message, extra=kwargs)

    def log_crypto_operation(self, operation, details, success=True):
        status = "SUCCESS" if success else "FAILURE"
        msg = f"CRYPTO_OP: {operation} | {status} | {details}"
        if success:
            self.log_info(msg)
        else:
            self.log_warning(msg)

    def log_key_generation(self, key_type, key_size):
        self.log_info(f"Generated {key_type} key of size {key_size} bits")

    def log_signature(self, tx_id, signature_valid):
        if signature_valid:
            self.log_info(f"Signature valid for tx {tx_id}")
        else:
            self.log_error(f"Invalid signature for tx {tx_id}")

if __name__ == "__main__":
    logger = CryptoLogger()
    logger.log_crypto_operation("encrypt", {"algorithm": "AES", "length": 256}, True)
    logger.log_key_generation("RSA", 2048)
    logger.log_signature("0x123def", True)
    logger.log_error("Test error for demo")