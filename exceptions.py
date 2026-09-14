import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

class NetworkError(Exception):
    """Base exception for crypto network failures."""
    pass

def retry_operation(retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise NetworkError(f"Max retries reached: {last_exception}") from last_exception
        return wrapper
    return decorator