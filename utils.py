import time
import logging
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger('python-utils-91')

def with_retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(
                        f"Attempt {attempt} failed for {func.__name__}: {e}. "
                        f"Retrying in {delay}s..."
                    )
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            logger.error(f"All {max_attempts} attempts failed for {func.__name__}.")
            raise last_exception
        return wrapper
    return decorator