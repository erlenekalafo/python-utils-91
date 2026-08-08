import time
import random

DEFAULT_MAX_RETRIES = 5
DEFAULT_BACKOFF_FACTOR = 0.5

# Defining some standard error class for network exceptions
class NetworkException(Exception):
    pass

# A function to implement exponential backoff retry logic

def retry_operation(func, max_retries=DEFAULT_MAX_RETRIES, backoff_factor=DEFAULT_BACKOFF_FACTOR, *args, **kwargs):
    retries = 0
    while retries < max_retries:
        try:
            return func(*args, **kwargs)
        except NetworkException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 1)
            time.sleep(wait_time)
            if retries == max_retries:
                raise e
    return None
