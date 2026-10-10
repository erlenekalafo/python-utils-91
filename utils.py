import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, backoff=2.0, exceptions=(Exception,)):
    """
    Decorator to retry network-bound operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = 1.0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Max retries reached for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Retrying {func.__name__} due to: {e}. Attempt {attempt}/{retries}")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator