import json
import logging
from typing import Dict, Any, Optional

# Configure logger for crypto data transactions
logger = logging.getLogger('python-utils-91')

def normalize_crypto_payload(raw_data: str) -> Optional[Dict[str, Any]]:
    """Parses and validates incoming raw crypto exchange data."""
    try:
        data = json.loads(raw_data)
        
        # Basic schema verification for price updates
        required_fields = {'pair', 'price', 'timestamp'}
        if not all(field in data for field in required_fields):
            logger.error(f"Invalid schema received: {data.keys()}")
            return None
            
        return {
            "pair": str(data['pair']).upper(),
            "price": float(data['price']),
            "timestamp": int(data['timestamp']),
            "volume": float(data.get('volume', 0.0))
        }
    except (json.JSONDecodeError, ValueError, KeyError) as e:
        logger.error(f"Data processing failure: {str(e)}")
        return None

def format_trade_event(event: Dict[str, Any]) -> str:
    """Serializes processed data for downstream persistence."""
    return json.dumps({
        "type": "TRADE_UPDATE",
        "payload": event
    })