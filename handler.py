import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("crypto-handler")

class CryptoTransactionHandler:
    """Handles incoming crypto payload normalization and validation."""

    def __init__(self, fee_rate: float = 0.001) -> None:
        self.fee_rate = fee_rate
        logger.info("Initialized CryptoTransactionHandler with fee rate %.4f", fee_rate)

    def calculate_net_amount(self, amount: float) -> float:
        """Deduct the configured fee from the raw transaction amount."""
        if amount <= 0:
            raise ValueError("Transaction amount must be strictly positive")
        fee = amount * self.fee_rate
        net_amount = amount - fee
        logger.debug("Calculated net amount: %.8f (fee: %.8f)", net_amount, fee)
        return net_amount

    def process_payload(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Clean and organize transaction payload data."""
        tx_id = payload.get("tx_id")
        raw_amount = payload.get("amount")

        if not tx_id or raw_amount is None:
            logger.warning("Invalid payload structure received: %s", payload)
            return None

        try:
            net = self.calculate_net_amount(float(raw_amount))
            return {
                "tx_id": str(tx_id),
                "net_amount": net,
                "status": "processed"
            }
        except (ValueError, TypeError) as exc:
            logger.error("Failed to process transaction %s: %s", tx_id, exc)
            return None
