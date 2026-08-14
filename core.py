import json

class CryptoProcessor:
    def __init__(self):
        self.supported_coins = ['BTC', 'ETH', 'LTC']

    def validate_input(self, coin):
        if coin not in self.supported_coins:
            raise ValueError(f'Unsupported coin: {coin}')

    def process_transaction(self, coin, amount):
        self.validate_input(coin)
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')
        # Placeholder for actual transaction processing
        return {'status': 'success', 'coin': coin, 'amount': amount}

    def main_loop(self, transactions):
        results = []
        for transaction in transactions:
            try:
                coin = transaction['coin']
                amount = transaction['amount']
                result = self.process_transaction(coin, amount)
                results.append(result)
            except ValueError as e:
                results.append({'status': 'error', 'message': str(e)})
        return json.dumps(results)

if __name__ == '__main__':
    transactions = [
        {'coin': 'BTC', 'amount': 0.1},
        {'coin': 'ETH', 'amount': 0.5},
        {'coin': 'DOGE', 'amount': 1},
        {'coin': 'LTC', 'amount': -1},
    ]
    processor = CryptoProcessor()
    output = processor.main_loop(transactions)
    print(output)