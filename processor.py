import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_network_op(exceptions: tuple[Type[Exception], ...], 
                     max_retries: int = 3, 
                     delay: float = 1.0) -> Callable:
    """Decorator to retry network-bound crypto operations."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error(f"Max retries reached. Final error: {last_exception}")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op((ConnectionError, TimeoutError))
def fetch_market_data(endpoint: str) -> dict:
    """Mock crypto exchange API fetch operation."""
    # Actual network logic would reside here
    return {"status": "success", "data": 0.0}
