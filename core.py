import time
import random
import logging
from functools import wraps
from typing import Callable, Type, Tuple, Any

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff.
    Useful for resilient crypto exchange API calls and RPC queries.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(f"Failed after {max_retries} attempts: {err}")
                        raise err
                    
                    jitter = random.uniform(0, 0.1 * delay)
                    sleep_time = delay + jitter
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed for {func.__name__}: {err}. "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor

        return wrapper
    return decorator


class CryptoNetworkClient:
    """Client wrapper for crypto network operations with failure tolerance."""

    def __init__(self, retries: int = 3):
        self.retries = retries

    @retry_network_op(max_retries=3, initial_delay=0.5, backoff_factor=2.0)
    def fetch_ticker(self, symbol: str) -> dict:
        """Simulates fetching ticker data from a crypto exchange."""
        if symbol.upper() not in ["BTC/USD", "ETH/USD", "SOL/USD"]:
            raise ValueError(f"Unsupported trading pair: {symbol}")
        return {"symbol": symbol, "price": 50000.0, "status": "ok"}
