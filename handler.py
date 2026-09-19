import re
from typing import Dict, Any, List, Optional


class CryptoTransactionHandler:
    """Processes raw cryptocurrency transaction payloads with strict input validation."""

    ALLOWED_CURRENCIES = {"BTC", "ETH", "SOL", "USDT"}
    ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")

    def __init__(self, max_batch_size: int = 100):
        self.max_batch_size = max_batch_size

    def validate_payload(self, raw_tx: Dict[str, Any]) -> Dict[str, Any]:
        """Validates transaction fields and raises ValueError if invalid."""
        if not isinstance(raw_tx, dict):
            raise ValueError("Payload must be a dictionary")

        tx_id = raw_tx.get("tx_id")
        if not tx_id or not isinstance(tx_id, str):
            raise ValueError("Missing or invalid 'tx_id'")

        symbol = str(raw_tx.get("symbol", "")).upper()
        if symbol not in self.ALLOWED_CURRENCIES:
            raise ValueError(f"Unsupported currency symbol: {symbol}")

        amount = raw_tx.get("amount")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError(f"Transaction amount must be a positive number: {amount}")

        recipient = raw_tx.get("recipient", "")
        if symbol == "ETH" and not self.ETH_ADDRESS_PATTERN.match(recipient):
            raise ValueError(f"Invalid Ethereum recipient address: {recipient}")

        return {
            "tx_id": tx_id,
            "symbol": symbol,
            "amount": float(amount),
            "recipient": recipient,
            "status": "VALIDATED",
        }

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop with payload validation and status reporting."""
        if len(batch) > self.max_batch_size:
            raise ValueError(f"Batch size exceeds limit of {self.max_batch_size}")

        processed_results = []
        for raw_tx in batch:
            try:
                validated_tx = self.validate_payload(raw_tx)
                processed_results.append(validated_tx)
            except ValueError as err:
                processed_results.append({
                    "tx_id": raw_tx.get("tx_id", "UNKNOWN") if isinstance(raw_tx, dict) else "UNKNOWN",
                    "status": "REJECTED",
                    "reason": str(err),
                })

        return processed_results
