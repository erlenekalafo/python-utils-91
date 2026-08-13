import logging
import logging.handlers

def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('CryptoLogger')
    logger.setLevel(logging.DEBUG)
    
    # Create a file handler that logs even debug messages
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)
    
    # Create a console handler for displaying logs in the terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)
    
    return logger

# Example of usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up and running!')