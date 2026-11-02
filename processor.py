import re
from typing import Dict, Any, List

ETH_ADDRESS_REGEX = r"^0x[a-fA-F0-9]{40}$"
ALLOWED_SYMBOLS = {"BTC", "ETH", "USDT", "SOL"}

class ProcessingError(Exception):
    """Custom exception raised when payload validation or execution fails."""
    pass

def validate_transaction_payload(payload: Dict[str, Any]) -> bool:
    """Validate incoming crypto transaction payload for required fields and formats."""
    required_fields = ["sender", "recipient", "amount", "symbol"]
    for field in required_fields:
        if field not in payload:
            raise ProcessingError(f"Missing required field: {field}")

    if not isinstance(payload["amount"], (int, float)) or payload["amount"] <= 0:
        raise ProcessingError("Amount must be a positive number")

    if payload["symbol"] not in ALLOWED_SYMBOLS:
        raise ProcessingError(f"Unsupported symbol: {payload['symbol']}")

    if not re.match(ETH_ADDRESS_REGEX, payload["sender"]):
        raise ProcessingError("Invalid sender Ethereum address format")

    if not re.match(ETH_ADDRESS_REGEX, payload["recipient"]):
        raise ProcessingError("Invalid recipient Ethereum address format")

    return True

def process_transaction_queue(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Main processing loop that validates and processes a list of transactions."""
    processed_results = []
    
    for idx, tx in enumerate(transactions):
        try:
            # Validate input payload before processing
            validate_transaction_payload(tx)
            
            # Simulate transaction processing
            result = {
                "tx_id": idx + 1,
                "status": "success",
                "amount": tx["amount"],
                "symbol": tx["symbol"],
                "from": tx["sender"],
                "to": tx["recipient"]
            }
            processed_results.append(result)
        except ProcessingError as err:
            processed_results.append({
                "tx_id": idx + 1,
                "status": "rejected",
                "reason": str(err)
            })
            
    return processed_results
