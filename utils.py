import logging

def validate_crypto_payload(data: dict) -> bool:
    """Validate transaction structure for crypto processing."""
    required_fields = {'asset', 'amount', 'wallet_address'}
    if not all(field in data for field in required_fields):
        return False
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return False
    if len(str(data['wallet_address'])) < 26:
        return False
    return True

def process_transactions(queue: list):
    """Main processing loop with validation."""
    logging.basicConfig(level=logging.INFO)
    for entry in queue:
        try:
            if not validate_crypto_payload(entry):
                logging.warning(f"Skipping invalid payload: {entry}")
                continue
            
            # Simulate secure processing of valid data
            asset = entry['asset']
            amount = entry['amount']
            logging.info(f"Processing {amount} units of {asset}")
        except Exception as e:
            logging.error(f"Critical processing failure: {e}")

if __name__ == "__main__":
    sample_data = [
        {"asset": "BTC", "amount": 0.5, "wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"},
        {"asset": "ETH", "amount": -1, "wallet_address": "invalid"}
    ]
    process_transactions(sample_data)