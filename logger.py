import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def exception(self, message):
        self.logger.exception(message)

# Example usage:
if __name__ == '__main__':
    log = Logger(__name__)
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.debug('This is a debug message')
    log.exception('This is an exception message')