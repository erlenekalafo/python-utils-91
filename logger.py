import logging

# Setting up a basic logger configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)

# Input validation function

def validate_input(user_input):
    if isinstance(user_input, str) and user_input:
        return True
    return False

if __name__ == '__main__':
    logger = Logger(__name__)
    while True:
        user_input = input('Enter a message to log (or "exit" to quit): ')
        if user_input.lower() == 'exit':
            logger.log_info('Exiting the program.')
            break
        if validate_input(user_input):
            logger.log_info(user_input)
        else:
            logger.log_warning('Invalid input. Please enter a non-empty string.')