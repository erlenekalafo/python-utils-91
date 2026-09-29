import logging

def validate_transaction(tx):
    """Ensures crypto transaction data is valid."""
    required_fields = {'sender', 'receiver', 'amount', 'currency'}
    if not all(field in tx for field in required_fields):
        return False
    if not isinstance(tx['amount'], (int, float)) or tx['amount'] <= 0:
        return False
    return True

def process_transactions(transactions):
    """Main processing loop with input validation."""
    processed_count = 0
    for tx in transactions:
        try:
            if not validate_transaction(tx):
                logging.warning(f"Invalid transaction skipped: {tx}")
                continue
            
            # Simulate secure crypto processing logic
            execute_transfer(tx)
            processed_count += 1
        except Exception as e:
            logging.error(f"Unexpected error during processing: {e}")
    return processed_count

def execute_transfer(tx):
    """Placeholder for internal crypto transfer logic."""
    pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sample_data = [
        {'sender': 'alice', 'receiver': 'bob', 'amount': 1.5, 'currency': 'BTC'},
        {'sender': 'bob', 'amount': -10, 'currency': 'ETH'},
        {'sender': 'charlie', 'receiver': 'dave', 'amount': 5}
    ]
    count = process_transactions(sample_data)
    print(f"Successfully processed {count} transactions")