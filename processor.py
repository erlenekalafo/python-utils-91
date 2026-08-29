import hashlib
import re
from typing import List, Dict, Any

def validate_crypto_address(address: str) -> bool:
    """Validate basic cryptocurrency address format."""
    if not address or not isinstance(address, str):
        return False
    # Basic validation for BTC and similar addresses
    pattern = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
    if not re.match(pattern, address):
        return False
    return True

def validate_amount(amount: float) -> bool:
    """Ensure amount is positive number."""
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False
    return True

class CryptoProcessor:
    """Handles crypto transaction processing with validation."""
    def __init__(self):
        self.processed_count = 0
        self.errors = []

    def process_transaction(self, tx_data: Dict[str, Any]) -> bool:
        """Validate and process individual transaction."""
        if not isinstance(tx_data, dict):
            self.errors.append("Invalid transaction data type")
            return False
        address = tx_data.get('address')
        amount = tx_data.get('amount')
        if not validate_crypto_address(address):
            self.errors.append(f"Invalid address: {address}")
            return False
        if not validate_amount(amount):
            self.errors.append(f"Invalid amount: {amount}")
            return False
        # Simulate crypto processing with hash
        tx_hash = hashlib.sha256(str(tx_data).encode()).hexdigest()[:16]
        self.processed_count += 1
        print(f"Processed transaction {tx_hash} for amount {amount} to {address}")
        return True

    def main_processing_loop(self, transactions: List[Dict[str, Any]]) -> None:
        """Main loop processing transactions with input validation."""
        for tx in transactions:
            if self.process_transaction(tx):
                print("Transaction completed successfully")
            else:
                print("Transaction skipped due to validation failure")
        print(f"Total transactions processed: {self.processed_count}")
        if self.errors:
            print(f"Encountered errors: {len(self.errors)}")

if __name__ == "__main__":
    processor = CryptoProcessor()
    sample_transactions = [
        {"address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "amount": 1.5},
        {"address": "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy", "amount": 0.25},
        {"address": "invalidaddress123", "amount": 10},
        {"address": "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2", "amount": -5}
    ]
    processor.main_processing_loop(sample_transactions)