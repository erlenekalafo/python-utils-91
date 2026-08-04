import time
import requests


def retry_request(url, max_retries=3, delay=2):
    """
    Makes a GET request to the specified URL with retry logic.
    Retries the request if it fails due to network-related exceptions.
    
    :param url: The URL to send the request to.
    :param max_retries: Maximum number of retry attempts.
    :param delay: Delay in seconds between retries.
    :return: The response object if the request is successful; raises an exception otherwise.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an error for bad responses
            return response
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(delay)  # Wait before retrying
                continue  # Try again
            else:
                raise e  # Raise the last exception if all retries failed


if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        response = retry_request(url)
        print(response.json())  # Process the successful response
    except Exception as e:
        print(f'Error occurred: {e}')  # Handle errors accordingly
