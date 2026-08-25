import time
from functools import wraps

def retry(max_attempts=3, initial_delay=1.0, backoff_factor=2.0, exceptions=(Exception,)):
    """Decorator for retry logic on network operations.
    This is practical for crypto module to handle API rate limits and transient errors.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            delay = initial_delay
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == max_attempts:
                        # All attempts failed, propagate the error
                        raise
                    time.sleep(delay)
                    delay *= backoff_factor
            # This line should not be reached
            raise RuntimeError("Unexpected end of retry logic")
        return wrapper
    return decorator