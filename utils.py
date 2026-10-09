import time
import random
from functools import wraps
from typing import Callable, Type, Union, Tuple, Any

def retry_on_failure(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = Exception
) -> Callable:
    """
    Decorator to retry a network or API function with exponential backoff and jitter.
    Useful for handling transient network drops or crypto API rate limiting.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        raise e
                    
                    # Exponential backoff with light randomized jitter
                    jitter = random.uniform(0, 0.1 * current_delay)
                    sleep_time = current_delay + jitter
                    
                    print(f"[Retry Warning] Attempt {attempt}/{retries} failed due to {e.__class__.__name__}. Retrying in {sleep_time:.2f}s...")
                    
                    time.sleep(sleep_time)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator