import json
from validators import validate_transaction_input

def process_transactions(transactions):
    processed_transactions = []
    for transaction in transactions:
        try:
            # Validate the input for each transaction
            if validate_transaction_input(transaction):
                # Process the transaction if valid
                processed_transaction = process_transaction(transaction)
                processed_transactions.append(processed_transaction)
            else:
                print(f'Invalid transaction input: {transaction}')
        except Exception as e:
            print(f'Error processing transaction: {e}')
    return processed_transactions


def process_transaction(transaction):
    # Mock transaction processing
    return { 'status': 'processed', 'data': transaction }

if __name__ == '__main__':
    sample_transactions = [
        {'amount': 100, 'currency': 'BTC', 'to': 'address1'},
        {'amount': -50, 'currency': 'ETH', 'to': 'address2'},  # Invalid amount
        {'amount': 200, 'currency': 'BTC', 'to': ''}  # Missing address
    ]
    results = process_transactions(sample_transactions)
    print(json.dumps(results, indent=2))