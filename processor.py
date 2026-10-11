from typing import List, Dict, Optional, Union

class CryptoProcessor:
    """Handles cryptographic data stream normalization and validation."""

    def __init__(self, key_size: int = 256) -> None:
        """Initialize processor with specified bit length."""
        self.key_size: int = key_size
        self.buffer: List[bytes] = []

    def normalize_payload(self, data: Union[str, bytes]) -> bytes:
        """Convert input to standard byte format for signing."""
        if isinstance(data, str):
            return data.encode('utf-8')
        return data

    def batch_process(self, items: List[Dict[str, str]]) -> List[bytes]:
        """Process a batch of dictionaries into validated byte sequences."""
        processed: List[bytes] = []
        for entry in items:
            raw_val = entry.get('payload', b'')
            if raw_val:
                processed.append(self.normalize_payload(raw_val))
        return processed

    def update_buffer(self, chunk: bytes) -> Optional[int]:
        """Add data chunk to buffer and return new size."""
        if not isinstance(chunk, bytes):
            raise TypeError("Buffer content must be bytes")
        self.buffer.append(chunk)
        return len(self.buffer)