import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=1):
    """
    Perform an HTTP GET request with retry logic.

    Args:
        url (str): The URL to request.
        max_retries (int): The maximum number of retries before failing.
        backoff_factor (float): The backoff factor for retry delay.

    Returns:
        Response: The HTTP response from the request.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            if attempt < max_retries - 1:
                sleep_time = backoff_factor * (2 ** attempt)
                time.sleep(sleep_time)
                continue
            else:
                raise e

# Example usage
if __name__ == '__main__':
    try:
        response = retry_request('https://api.example.com/data')
        print(response.json())
    except Exception as ex:
        print(f'Failed to retrieve data: {ex}')