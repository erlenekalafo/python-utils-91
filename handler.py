import json
from constants import TRANSACTION_STATUS
from exceptions import TransactionError

class TransactionHandler:
    def __init__(self, transaction_data):
        self.transaction_data = transaction_data
        self.validate_transaction()

    def validate_transaction(self):
        if not self.transaction_data.get('amount') > 0:
            raise TransactionError('Invalid transaction amount')
        if self.transaction_data.get('status') not in TRANSACTION_STATUS:
            raise TransactionError('Invalid transaction status')

    def process_transaction(self):
        # Simulate transaction processing
        print(f'Processing transaction: {json.dumps(self.transaction_data)}')
        return {'status': 'success', 'transaction': self.transaction_data}

    def log_transaction(self):
        # Log transaction details
        print(f'Transaction details: {self.transaction_data}')