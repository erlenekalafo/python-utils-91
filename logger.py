import logging

class CustomLogger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Error logging info: {str(e)}')

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error(f'Error logging warning: {str(e)}')

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f'Error logging error: {str(e)}')

# Example usage
if __name__ == '__main__':
    custom_logger = CustomLogger(__name__)
    custom_logger.log_info('This is an info message.')
    custom_logger.log_warning('This is a warning message.')
    custom_logger.log_error('This is an error message.')