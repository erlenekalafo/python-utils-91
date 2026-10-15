import time
import logging
import random
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator for retrying crypto API network operations with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    if attempt == max_retries:
                        logger.error(f"Operation {func.__name__} failed after {max_retries} attempts: {exc}")
                        raise
                    
                    sleep_time = delay
                    if jitter:
                        sleep_time += random.uniform(0, 0.5)
                    
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for {func.__name__} failed: {exc}. "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor
        return wrapper
    return decorator


class CryptoDataProcessor:
    """Processor for executing crypto exchange requests with retry resiliency."""

    def __init__(self, retries: int = 3):
        self.retries = retries

    @retry_network_op(max_retries=3, initial_delay=0.5, backoff_factor=2.0)
    def fetch_order_book(self, symbol: str) -> dict:
        """Fetch order book data from exchange endpoint with automatic retries."""
        if random.random() < 0.3:
            raise ConnectionError(f"Transient network failure for {symbol} order book endpoint")
        return {"symbol": symbol, "bids": [[50000.0, 1.2]], "asks": [[50010.0, 0.8]]}
