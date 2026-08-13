import json
from typing import Any, Dict, List, Union

def parse_crypto_data(data: Union[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Parses crypto data from JSON string or dictionary format."""
    if isinstance(data, str):
        try:
            # Convert JSON string to dictionary
            data = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON string')

    if not isinstance(data, dict):
        raise TypeError('Input must be a string or a dictionary')

    # Extracting relevant crypto data
    crypto_list = []
    for key, value in data.items():
        if isinstance(value, dict) and 'price' in value and 'symbol' in value:
            crypto_info = {
                'symbol': value['symbol'],
                'price': value['price'],
                'timestamp': value.get('timestamp', None)
            }
            crypto_list.append(crypto_info)
    return crypto_list

def save_to_file(filename: str, data: List[Dict[str, Any]]) -> None:
    """Saves the parsed crypto data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    sample_data = '{ "BTC": { "symbol": "BTC", "price": "50000", "timestamp": "2023-10-01" }, "ETH": { "symbol": "ETH", "price": "4000" } }'
    parsed_data = parse_crypto_data(sample_data)
    save_to_file('crypto_data.json', parsed_data)