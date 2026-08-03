MAX_RETRIES = 5
TIMEOUT = 30
API_ENDPOINT = 'https://api.example.com'
STATUS_CODES = {
    'OK': 200,
    'CREATED': 201,
    'NO_CONTENT': 204,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'INTERNAL_SERVER_ERROR': 500,
}

DEFAULT_SETTINGS = {
    'retries': MAX_RETRIES,
    'timeout': TIMEOUT,
}

LOGGING_LEVELS = {
    'DEBUG': 'DEBUG',
    'INFO': 'INFO',
    'WARNING': 'WARNING',
    'ERROR': 'ERROR',
    'CRITICAL': 'CRITICAL',
}

SUPPORTED_FORMATS = ['json', 'xml', 'csv']

API_KEYS = {
    'service_x': 'YOUR_API_KEY_FOR_SERVICE_X',
    'service_y': 'YOUR_API_KEY_FOR_SERVICE_Y',
}
