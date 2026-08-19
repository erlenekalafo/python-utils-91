import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, backoff_factor=0.3):
    """Performs a GET request with retry logic on failure."""
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response if successful
        except RequestException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1))
            print(f"Attempt {retries} failed: {e}. Retrying in {wait_time:.1f} seconds...")
            time.sleep(wait_time)
    raise Exception(f"Max retries exceeded for URL: {url}")