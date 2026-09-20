import hashlib
from typing import Tuple, Union

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_decode(v: str) -> bytes:
    """Decodes a base58 encoded string into bytes, handling leading zero bytes."""
    decimal = 0
    for char in v:
        decimal = decimal * 58 + BASE58_ALPHABET.index(char)
    
    # Preserve leading zero bytes (represented as '1' in Bitcoin base58)
    n_pad = len(v) - len(v.lstrip('1'))
    decoded_bytes = decimal.to_bytes((decimal.bit_length() + 7) // 8, byteorder='big')
    return b'\x00' * n_pad + decoded_bytes


def validate_bitcoin_address(address: Union[str, None]) -> Tuple[bool, str]:
    """Validates a legacy Bitcoin mainnet address with strict checksum logic and error handling."""
    if not address:
        return False, "empty address value"

    if not isinstance(address, str):
        return False, "address must be a string type"

    if len(address) < 26 or len(address) > 35:
        return False, f"invalid address length: {len(address)}"

    if not (address.startswith("1") or address.startswith("3")):
        return False, "invalid address prefix, must start with 1 or 3"

    try:
        # Verify characters are within the base58 alphabet
        for char in address:
            if char not in BASE58_ALPHABET:
                return False, f"invalid base58 character '{char}' detected"

        decoded = base58_decode(address)
        
        # Legacy address payload + checksum must total 25 bytes
        if len(decoded) != 25:
            return False, "invalid decoded payload length"

        payload = decoded[:-4]
        checksum = decoded[-4:]

        # Double SHA-256 for legacy checksum validation
        first_sha = hashlib.sha256(payload).digest()
        second_sha = hashlib.sha256(first_sha).digest()

        if second_sha[:4] != checksum:
            return False, "checksum validation failed"

        return True, "valid legacy address"

    except ValueError as val_err:
        return False, f"value parsing failure: {str(val_err)}"
    except Exception as err:
        return False, f"unexpected validation failure: {str(err)}"
