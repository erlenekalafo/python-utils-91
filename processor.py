import json
import requests
from typing import List

class CryptoProcessor:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.cache = {}

    def fetch_data(self, coin_ids: List[str]) -> dict:
        # Use cached results if available
        data_to_fetch = [coin for coin in coin_ids if coin not in self.cache]
        if not data_to_fetch:
            return self.get_cached_data(coin_ids)

        response = requests.get(self.api_url, params={'ids': ','.join(data_to_fetch)})
        response.raise_for_status()
        data = response.json()

        # Cache the fetched data
        for coin in data:
            self.cache[coin['id']] = coin

        return {coin_id: self.cache[coin_id] for coin_id in coin_ids}

    def get_cached_data(self, coin_ids: List[str]) -> dict:
        return {coin_id: self.cache[coin_id] for coin_id in coin_ids if coin_id in self.cache}

# Example of usage:
if __name__ == '__main__':
    processor = CryptoProcessor('https://api.coingecko.com/api/v3/coins/markets')
    data = processor.fetch_data(['bitcoin', 'ethereum'])
    print(json.dumps(data, indent=2))