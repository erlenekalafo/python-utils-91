import logging

def validate_crypto_payload(data):
    """Ensures payload meets minimum requirements."""
    required_keys = {'asset', 'amount', 'timestamp'}
    if not isinstance(data, dict) or not required_keys.issubset(data.keys()):
        return False
    if data['amount'] <= 0:
        return False
    return True

def run_processor(data_stream):
    """Main processing loop with integrated input validation."""
    logger = logging.getLogger(__name__)
    
    for entry in data_stream:
        if not validate_crypto_payload(entry):
            logger.warning(f"Discarding invalid packet: {entry}")
            continue
        
        try:
            # Simulate transaction processing
            process_trade(entry)
        except Exception as e:
            logger.error(f"Execution error on asset {entry['asset']}: {e}")

def process_trade(trade):
    """Executes the trade logic."""
    # Placeholder for actual crypto execution logic
    pass

if __name__ == '__main__':
    sample_data = [{'asset': 'BTC', 'amount': 0.5, 'timestamp': 1672531200}, {'asset': 'ETH', 'amount': -1, 'timestamp': 1672531205}]
    run_processor(sample_data)