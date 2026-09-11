import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = 1
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == retries:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator