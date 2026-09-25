import logging

def validate_crypto_payload(data: dict) -> bool:
    """Ensures payload contains valid keys for processing."""
    required = {'symbol', 'amount', 'timestamp'}
    if not all(key in data for key in required):
        return False
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return False
    return True

def process_stream(data_stream: list):
    """Main loop processing incoming crypto data."""
    logger = logging.getLogger(__name__)
    
    for entry in data_stream:
        if not isinstance(entry, dict):
            logger.warning("Malformed stream entry: non-dict")
            continue
            
        if not validate_crypto_payload(entry):
            logger.error(f"Invalid crypto payload skipped: {entry.get('symbol')}")
            continue
            
        # Core processing logic for verified data
        try:
            symbol = entry['symbol']
            amount = entry['amount']
            print(f"Processing {amount} units of {symbol}")
        except KeyError as e:
            logger.critical(f"Critical processing failure: {e}")

if __name__ == "__main__":
    sample_data = [
        {'symbol': 'BTC', 'amount': 0.5, 'timestamp': 1625097600},
        {'symbol': 'ETH', 'amount': -1, 'timestamp': 1625097600},
        {'invalid': 'data'}
    ]
    process_stream(sample_data)