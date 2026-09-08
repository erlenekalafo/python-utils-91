import time
import random
import functools
import urllib.request
import urllib.error
import json

def with_retry(retries=3, backoff_factor=2.0, exceptions=(urllib.error.URLError,)):
    """Decorator for retrying network operations with exponential backoff and jitter."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = 1.0
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        raise e
                    # Apply exponential backoff with a small random jitter
                    sleep_time = (delay * (backoff_factor ** attempt)) + random.uniform(0, 0.5)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@with_retry(retries=3, backoff_factor=1.5)
def fetch_crypto_price(ticker: str) -> dict:
    """Fetches current price for a crypto ticker from a public API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ticker}&vs_currencies=usd"
    req = urllib.request.Request(
        url, 
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=5) as response:
        return json.loads(response.read().decode())
