import time
import random
import functools

def retry_network(
    max_retries: int = 3,
    delay_seconds: float = 1,
    backoff_multiplier: float = 2,
    exceptions: tuple = (Exception,)
):
    """Retry decorator for network operations with exponential backoff and jitter.

    Useful for crypto API calls that may face rate limits or temporary failures.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            current_delay = delay_seconds
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exc = exc
                    if attempt == max_retries - 1:
                        break
                    # Exponential backoff with jitter to avoid thundering herd
                    sleep_time = current_delay + random.uniform(0, 0.5)
                    time.sleep(sleep_time)
                    current_delay *= backoff_multiplier
            if last_exc:
                raise last_exc
            # Should not reach here
            raise RuntimeError("Retry logic failed unexpectedly")
        return wrapper
    return decorator

# Example of a network operation for crypto context
def get_crypto_price(coin_id: str) -> float:
    """Simulated network call to get crypto price.

    In production, replace with actual API call.
    """
    # Simulate occasional network issues
    if random.random() < 0.3:  # 30% chance of failure for demo
        raise ConnectionError(f"Failed to fetch price for {coin_id}")
    # Simulated price data
    prices = {"bitcoin": 65000.0, "ethereum": 2500.0}
    return prices.get(coin_id, 100.0)

# Apply retry logic
@retry_network(max_retries=4, delay_seconds=0.5, backoff_multiplier=1.5)
def fetch_with_retry(coin_id: str) -> float:
    """Wrapper using retry for reliable crypto data retrieval."""
    return get_crypto_price(coin_id)

# Test the function if run directly
if __name__ == "__main__":
    try:
        price = fetch_with_retry("bitcoin")
        print(f"Successfully fetched price: {price}")
    except Exception as e:
        print(f"Failed after retries: {e}")