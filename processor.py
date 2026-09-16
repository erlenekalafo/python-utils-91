import logging
from typing import Any, Dict

def validate_crypto_payload(data: Dict[str, Any]) -> bool:
    """Validates transaction structure for crypto processing."""
    required_keys = {'asset', 'amount', 'address'}
    if not all(key in data for key in required_keys):
        return False
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return False
    return len(str(data['address'])) >= 26

def run_processing_loop(data_stream: list):
    """Main loop with input validation for stream processing."""
    logging.basicConfig(level=logging.INFO)
    for entry in data_stream:
        try:
            if not isinstance(entry, dict):
                logging.warning(f"Invalid data type: {type(entry)}")
                continue

            if not validate_crypto_payload(entry):
                logging.error(f"Validation failed for entry: {entry}")
                continue

            process_transaction(entry)
        except Exception as e:
            logging.error(f"Unexpected processing error: {e}")

def process_transaction(data: Dict[str, Any]):
    """Simulates secure crypto transaction handling."""
    logging.info(f"Processing {data['asset']} transfer of {data['amount']}")

if __name__ == '__main__':
    sample_data = [
        {'asset': 'BTC', 'amount': 0.5, 'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'},
        {'asset': 'ETH', 'amount': -1, 'address': 'invalid'},
        {'invalid': 'data'}
    ]
    run_processing_loop(sample_data)