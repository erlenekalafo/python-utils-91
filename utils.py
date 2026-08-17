import json
from datetime import datetime


def format_crypto_data(data):
    """Format raw crypto data for better readability."""
    formatted_data = []
    for item in data:
        formatted_item = {
            'symbol': item.get('symbol'),
            'price': round(float(item.get('price', 0)), 2),
            'timestamp': datetime.utcfromtimestamp(item.get('timestamp')).strftime('%Y-%m-%d %H:%M:%S'),
            'volume': round(float(item.get('volume', 0)), 2),
        }
        formatted_data.append(formatted_item)
    return json.dumps(formatted_data, indent=4)


def filter_by_symbol(data, symbol):
    """Filter crypto data by specific symbol."""
    return [item for item in data if item.get('symbol') == symbol]


def calculate_market_cap(price, volume):
    """Calculate market cap from price and volume."""
    return round(price * volume, 2)


if __name__ == '__main__':
    sample_data = [
        {'symbol': 'BTC', 'price': '45000.00', 'timestamp': 1633046400, 'volume': '1200.0'},
        {'symbol': 'ETH', 'price': '3000.00', 'timestamp': 1633046400, 'volume': '5000.0'},
    ]
    print(format_crypto_data(sample_data))
    print(filter_by_symbol(sample_data, 'BTC'))
    print(calculate_market_cap(45000.00, 1200.0))