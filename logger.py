import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=5):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage if this module is run directly
if __name__ == '__main__':
    log = setup_logger()
    log.debug('This is a debug message')
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical message')
