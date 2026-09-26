import re
from typing import Any, Dict, List, Tuple


class TransactionProcessor:
    """Processes and validates raw cryptocurrency transaction payloads."""

    SUPPORTED_CURRENCIES = {"BTC", "ETH", "USDT", "SOL"}
    ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")

    def __init__(self, min_amount: float = 0.0001):
        self.min_amount = min_amount

    def validate_payload(self, raw_tx: Dict[str, Any]) -> Tuple[bool, str]:
        """Validates structure and values of a transaction payload."""
        if not isinstance(raw_tx, dict):
            return False, "Payload must be a dictionary"

        tx_hash = raw_tx.get("tx_hash")
        amount = raw_tx.get("amount")
        address = raw_tx.get("address")
        currency = raw_tx.get("currency")

        if not tx_hash or not isinstance(tx_hash, str) or len(tx_hash) < 10:
            return False, "Invalid or missing tx_hash"

        if not isinstance(amount, (int, float)) or amount < self.min_amount:
            return False, f"Amount must be a number >= {self.min_amount}"

        if not address or not isinstance(address, str):
            return False, "Invalid or missing recipient address"

        if currency == "ETH" and not self.ETH_ADDRESS_REGEX.match(address):
            return False, "Invalid Ethereum address format"

        if currency not in self.SUPPORTED_CURRENCIES:
            return False, f"Unsupported currency: {currency}"

        return True, "Valid"

    def process_batch(self, raw_transactions: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Main processing loop with payload input validation."""
        processed = []
        rejected = []

        for raw_tx in raw_transactions:
            is_valid, reason = self.validate_payload(raw_tx)
            if not is_valid:
                rejected.append({"payload": raw_tx, "reason": reason})
                continue

            tx_data = {
                "tx_hash": raw_tx["tx_hash"],
                "amount": float(raw_tx["amount"]),
                "address": raw_tx["address"],
                "currency": raw_tx["currency"].upper(),
                "status": "QUEUED",
            }
            processed.append(tx_data)

        return {"processed": processed, "rejected": rejected}
