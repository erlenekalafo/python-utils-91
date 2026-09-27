import functools
import hashlib
from typing import Callable, Any, Dict

# Cache for crypto hash calculations to reduce redundant compute
_HASH_CACHE: Dict[tuple, str] = {}

@functools.lru_cache(maxsize=1024)
def compute_sha256(data: bytes) -> str:
    """Performs memory-optimized SHA256 hashing."""
    return hashlib.sha256(data).hexdigest()

def batch_process_signatures(data_list: list[bytes]) -> list[str]:
    """Optimized batch processor for signature generation."""
    return [compute_sha256(d) for d in data_list]

class CryptoEngine:
    def __init__(self, buffer_size: int = 4096):
        self.buffer_size = buffer_size

    def stream_hash(self, file_path: str) -> str:
        """Memory-efficient hashing for large crypto blobs."""
        hasher = hashlib.sha256()
        with open(file_path, "rb", buffering=self.buffer_size) as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()