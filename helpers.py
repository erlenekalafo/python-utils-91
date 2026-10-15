import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on exception."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (2 ** attempt))
            logger.error(f"Operation failed after {max_retries} attempts")
            raise last_exception
        return wrapper
    return decorator

def execute_with_retry(func: Callable, *args, **kwargs) -> Any:
    """Utility for executing arbitrary callables with retry."""
    return retry_on_failure()(func)(*args, **kwargs)