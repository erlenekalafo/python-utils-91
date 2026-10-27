import hashlib
import secrets
import json
from typing import Any, Dict

def generate_nonce(length: int = 32) -> str:
    """Generates a cryptographically secure random string."""
    return secrets.token_hex(length)

def compute_sha256(data: str) -> str:
    """Calculates SHA-256 hash of a string input."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def safe_json_dump(data: Dict[str, Any]) -> str:
    """Serializes dictionary to sorted keys JSON."""
    return json.dumps(data, sort_keys=True)

def validate_checksum(data: str, expected_hash: str) -> bool:
    """Verifies data integrity against provided hash."""
    return compute_sha256(data) == expected_hash

def mask_address(address: str, visible: int = 4) -> str:
    """Truncates crypto address for secure display."""
    if len(address) <= visible * 2:
        return address
    return f"{address[:visible]}...{address[-visible:]}"