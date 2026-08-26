class CryptoUtilsError(Exception):
    """Base exception for all python-utils-91 crypto errors."""
    pass


class InvalidKeyLengthError(CryptoUtilsError):
    """Raised when a cryptographic key does not match expected byte length."""
    def __init__(self, expected: int, actual: int, message: str = None):
        self.expected = expected
        self.actual = actual
        super().__init__(message or f"Invalid key length: expected {expected} bytes, got {actual} bytes")


class DecryptionError(CryptoUtilsError):
    """Raised when ciphertext decryption fails due to corruption or tampering."""
    def __init__(self, message: str = "Decryption failed: integrity check or padding error"):
        super().__init__(message)


class UnsupportedAlgorithmError(CryptoUtilsError):
    """Raised when an unsupported cipher or hash algorithm is requested."""
    def __init__(self, algorithm: str):
        self.algorithm = algorithm
        super().__init__(f"Unsupported cryptographic algorithm: '{algorithm}'")
