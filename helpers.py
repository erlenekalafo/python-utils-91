import time
import random
from functools import wraps

import requests


def retry_network_operation(max_retries=3, base_delay=1.0, max_delay=60.0):
    """Decorator to add retry logic to network operations.

    Uses exponential backoff with jitter for practical reliability.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, OSError, ConnectionError) as exc:
                    last_exception = exc
                    if attempt == max_retries - 1:
                        break
                    # Exponential backoff with jitter
                    delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
                    time.sleep(delay)
            if last_exception:
                raise last_exception
            raise RuntimeError("Unexpected retry failure")
        return wrapper
    return decorator


# Example function using the retry logic for a crypto-related network call
@retry_network_operation(max_retries=5, base_delay=2.0)
def get_crypto_data(coin_id):
    """Fetch data from a crypto API with automatic retries."""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


# Another utility for general network retries
def execute_with_retry(operation, *args, max_retries=3, **kwargs):
    """Execute a callable with retry logic."""
    last_exc = None
    for attempt in range(max_retries):
        try:
            return operation(*args, **kwargs)
        except Exception as exc:
            last_exc = exc
            if attempt == max_retries - 1:
                break
            delay = 2 ** attempt
            time.sleep(delay)
    raise last_exc