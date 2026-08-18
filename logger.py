import logging
import logging.handlers

def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    """Set up a logger with rotation configuration."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler with rotation
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger setup complete.')