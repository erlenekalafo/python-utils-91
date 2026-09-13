import re
from typing import List, Dict, Any

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def validate_transaction(tx: Dict[str, Any]) -> bool:
    """Validate a single transaction dictionary for required fields and formats."""
    if not isinstance(tx, dict):
        return False
    
    sender = tx.get("sender")
    recipient = tx.get("recipient")
    amount = tx.get("amount")

    if not sender or not ETH_ADDRESS_PATTERN.match(str(sender)):
        return False
    if not recipient or not ETH_ADDRESS_PATTERN.match(str(recipient)):
        return False
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False

    return True


def process_transaction_queue(queue: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Main processing loop with input validation for incoming crypto transactions."""
    processed = []
    rejected = []

    for item in queue:
        try:
            if validate_transaction(item):
                item_copy = item.copy()
                item_copy["status"] = "processed"
                processed.append(item_copy)
            else:
                item_copy = item.copy() if isinstance(item, dict) else {"raw": item}
                item_copy["status"] = "rejected"
                item_copy["reason"] = "invalid_format_or_values"
                rejected.append(item_copy)
        except Exception as err:
            rejected.append({"raw": str(item), "status": "failed", "reason": str(err)})

    return {"processed": processed, "rejected": rejected}
