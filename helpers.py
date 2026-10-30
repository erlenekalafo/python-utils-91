import re

# regex patterns for crypto address validation
ETH_ADDR_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
BTC_ADDR_PATTERN = re.compile(r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$')

def validate_crypto_input(data: dict) -> bool:
    """Validates address and amount fields in incoming payloads."""
    address = data.get("address", "")
    amount = data.get("amount", 0)

    # check if amount is a positive numeric type
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False

    # route validation based on expected asset type
    asset = data.get("asset", "").upper()
    if asset == "ETH":
        return bool(ETH_ADDR_PATTERN.match(address))
    elif asset == "BTC":
        return bool(BTC_ADDR_PATTERN.match(address))

    return False

def process_transaction_loop(queue):
    """Main loop with input validation check."""
    for tx in queue:
        if not validate_crypto_input(tx):
            print(f"Skipping invalid transaction: {tx.get('id')}")
            continue
        
        # logic for processing validated transactions
        execute_transfer(tx)

def execute_transfer(tx):
    """Mock execution function for validated items."""
    print(f"Processing transaction {tx.get('id')} of {tx.get('amount')}")