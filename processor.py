import logging
import re
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")


class TransactionProcessor:
    """Processes incoming crypto transactions with input validation."""

    def __init__(self, min_fee_gwei: float = 1.0):
        self.min_fee_gwei = min_fee_gwei
        self.processed_tx_hashes = set()

    def _is_valid_payload(self, tx: Dict[str, Any]) -> bool:
        """Validates payload fields and data types for a single transaction."""
        required_fields = {"tx_hash", "sender", "recipient", "amount", "fee_gwei"}
        if not isinstance(tx, dict) or not required_fields.issubset(tx.keys()):
            logger.warning("Transaction payload missing required keys")
            return False

        if not ADDRESS_REGEX.match(tx["sender"]) or not ADDRESS_REGEX.match(tx["recipient"]):
            logger.warning(f"Invalid address format in tx {tx.get('tx_hash')}")
            return False

        if not isinstance(tx["amount"], (int, float)) or tx["amount"] <= 0:
            logger.warning(f"Invalid transfer amount: {tx.get('amount')}")
            return False

        if not isinstance(tx["fee_gwei"], (int, float)) or tx["fee_gwei"] < self.min_fee_gwei:
            logger.warning(f"Fee below minimum threshold: {tx.get('fee_gwei')}")
            return False

        return True

    def process_queue(self, incoming_queue: List[Dict[str, Any]]) -> List[str]:
        """Main loop validating and recording incoming crypto transactions."""
        processed_batch = []

        for raw_tx in incoming_queue:
            if not self._is_valid_payload(raw_tx):
                logger.error("Skipping invalid transaction payload")
                continue

            tx_hash = raw_tx["tx_hash"]
            if tx_hash in self.processed_tx_hashes:
                logger.info(f"Duplicate transaction skipped: {tx_hash}")
                continue

            self.processed_tx_hashes.add(tx_hash)
            processed_batch.append(tx_hash)
            logger.info(f"Successfully verified tx {tx_hash}")

        return processed_batch
