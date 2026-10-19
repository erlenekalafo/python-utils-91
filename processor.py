import re
from typing import Dict, List, Any


class TransactionProcessor:
    """Processes incoming cryptocurrency transaction payloads with strict validation."""

    SUPPORTED_ASSETS = {"BTC", "ETH", "USDT", "SOL"}
    ADDRESS_PATTERNS = {
        "BTC": r"^(1|3|bc1)[a-zA-zA-HJ-NP-Z0-9]{25,62}$",
        "ETH": r"^0x[a-fA-F0-9]{40}$",
        "USDT": r"^0x[a-fA-F0-9]{40}$",
        "SOL": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$",
    }

    def validate_payload(self, raw_tx: Dict[str, Any]) -> tuple[bool, str]:
        """Validate raw transaction fields before processing."""
        if not isinstance(raw_tx, dict):
            return False, "Payload must be a dictionary"

        asset = raw_tx.get("asset")
        if asset not in self.SUPPORTED_ASSETS:
            return False, f"Unsupported or missing asset: {asset}"

        amount = raw_tx.get("amount")
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False, f"Invalid amount: {amount}. Must be positive number"

        address = raw_tx.get("recipient")
        if not address or not isinstance(address, str):
            return False, "Missing or invalid recipient address format"

        pattern = self.ADDRESS_PATTERNS.get(asset)
        if pattern and not re.match(pattern, address):
            return False, f"Recipient address format invalid for {asset}"

        return True, "Valid"

    def process_batch(self, batch: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Main processing loop with input validation for crypto payload batch."""
        successful = []
        failed = []

        for index, raw_payload in enumerate(batch):
            is_valid, reason = self.validate_payload(raw_payload)
            if not is_valid:
                failed.append({"index": index, "payload": raw_payload, "error": reason})
                continue

            tx_id = f"tx_{index}_{raw_payload['asset'].lower()}"
            processed_record = {
                "id": tx_id,
                "asset": raw_payload["asset"],
                "amount": float(raw_payload["amount"]),
                "recipient": raw_payload["recipient"],
                "status": "queued"
            }
            successful.append(processed_record)

        return {
            "processed_count": len(successful),
            "failed_count": len(failed),
            "successful": successful,
            "failed": failed
        }
