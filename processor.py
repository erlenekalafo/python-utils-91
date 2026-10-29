import re
from typing import Any, Dict, List

BTC_ADDRESS_REGEX = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
ETH_ADDRESS_REGEX = r"^0x[a-fA-F0-9]{40}$"
SUPPORTED_ASSETS = {"BTC", "ETH", "USDT", "SOL"}


class ValidationError(Exception):
    """Raised when incoming payload fails input validation."""

    pass


class TransactionProcessor:
    """Processes incoming crypto transactions with input validation."""

    def __init__(self) -> None:
        self.processed_count = 0
        self.failed_count = 0

    def validate_transaction(self, tx: Dict[str, Any]) -> None:
        """Validates structure and field types of a crypto transaction."""
        if not isinstance(tx, dict):
            raise ValidationError("Transaction payload must be a dictionary")

        required_keys = {"tx_id", "symbol", "recipient", "amount"}
        missing_keys = required_keys - tx.keys()
        if missing_keys:
            raise ValidationError(
                f"Missing required fields: {', '.join(missing_keys)}"
            )

        symbol = str(tx["symbol"]).upper()
        if symbol not in SUPPORTED_ASSETS:
            raise ValidationError(f"Unsupported crypto asset: {tx['symbol']}")

        amount = tx["amount"]
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValidationError(
                f"Invalid amount {amount}: must be a positive number"
            )

        recipient = str(tx["recipient"])
        if symbol in ("ETH", "USDT"):
            if not re.match(ETH_ADDRESS_REGEX, recipient):
                raise ValidationError(
                    f"Invalid Ethereum address format: {recipient}"
                )
        elif symbol == "BTC":
            if not re.match(BTC_ADDRESS_REGEX, recipient):
                raise ValidationError(
                    f"Invalid Bitcoin address format: {recipient}"
                )

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop that validates and prepares transaction batch."""
        successful_txs = []

        for raw_tx in batch:
            try:
                # Validate input fields before processing
                self.validate_transaction(raw_tx)

                # Transform and queue valid transaction
                processed_tx = {
                    "tx_id": str(raw_tx["tx_id"]),
                    "symbol": str(raw_tx["symbol"]).upper(),
                    "recipient": str(raw_tx["recipient"]),
                    "amount": float(raw_tx["amount"]),
                    "status": "VALIDATED",
                }
                successful_txs.append(processed_tx)
                self.processed_count += 1

            except ValidationError:
                self.failed_count += 1
                # Skip invalid payload safely without halting loop
                continue

        return successful_txs
