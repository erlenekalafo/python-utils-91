from typing import List, Dict, Optional

class CryptoProcessor:
    """Handles cryptographic data transformation and validation tasks."""

    def __init__(self, key_version: int = 1) -> None:
        self.key_version: int = key_version

    def process_payload(self, data: List[Dict[str, str]]) -> Dict[str, bool]:
        """
        Validates and marks payload entries based on hex integrity.

        Args:
            data: A list of dictionaries containing raw crypto hex strings.

        Returns:
            A mapping of hex keys to their validity status.
        """
        results: Dict[str, bool] = {}
        for entry in data:
            raw_val: Optional[str] = entry.get("hex")
            if raw_val and self._is_valid_hex(raw_val):
                results[raw_val] = True
            else:
                results[raw_val or "unknown"] = False
        return results

    def _is_valid_hex(self, value: str) -> bool:
        """
        Checks if a string is a valid hexadecimal sequence.
        """
        try:
            int(value, 16)
            return len(value) % 2 == 0
        except ValueError:
            return False

    def get_summary(self, results: Dict[str, bool]) -> str:
        """
        Generates a human-readable summary of processed crypto records.
        """
        passed: int = sum(1 for v in results.values() if v)
        return f"Processed {len(results)} items: {passed} valid, {len(results) - passed} invalid."