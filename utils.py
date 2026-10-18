import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_network_operation(exceptions: Tuple[Type[Exception], ...], 
                            max_retries: int = 3, 
                            delay: float = 1.0) -> Callable:
    """Decorator for retrying network operations on specific exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Operation failed after {max_retries} attempts")
            raise last_exception
        return wrapper
    return decorator