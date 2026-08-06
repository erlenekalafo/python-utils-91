from typing import Final, Tuple, Dict

# Constants for application configuration

# Database configuration constants
DATABASE_URL: Final[str] = "sqlite:///app.db"
DATABASE_TIMEOUT: Final[int] = 30

# HTTP Status Codes
STATUS_OK: Final[int] = 200
STATUS_NOT_FOUND: Final[int] = 404
STATUS_INTERNAL_SERVER_ERROR: Final[int] = 500

# Default settings
DEFAULT_SETTINGS: Final[Dict[str, str]] = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": "true"
}

# Supported file formats
SUPPORTED_FILE_FORMATS: Final[Tuple[str, ...]] = ("csv", "json", "xml")

# API Endpoints
API_ENDPOINTS: Final[Dict[str, str]] = {
    "get_user": "/api/user",
    "create_user": "/api/user/create",
    "update_user": "/api/user/update",
    "delete_user": "/api/user/delete"
}

# Timeout values
REQUEST_TIMEOUT: Final[int] = 10  # in seconds
