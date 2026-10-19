import time
import random
import functools
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

class CryptoNetworkError(Exception):
    """Raised when a crypto API or RPC network operation fails."""
    pass

def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff and jitter.
    
    Useful for resilient crypto exchange API calls and RPC queries.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Final retry attempt failed for {func.__name__}: {err}"
                        )
                        raise
                    
                    # Apply exponential backoff with full jitter
                    sleep_time = delay * (0.5 + random.random())
                    logger.warning(
                        f"Network op {func.__name__} failed (attempt {attempt}/{max_retries}): "
                        f"{err}. Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator
