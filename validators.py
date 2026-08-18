def validate_address(address: str) -> bool:
    """
    Validate a cryptocurrency address format.
    """
    if not isinstance(address, str):
        return False
    return len(address) in {34, 42} and address.startswith(('0x', '1', '3'))


def validate_amount(amount: float) -> bool:
    """
    Validate that the amount is a positive float.
    """
    return isinstance(amount, (int, float)) and amount > 0


def validate_transaction(transaction: dict) -> bool:
    """
    Validate the structure of a cryptocurrency transaction.
    """
    required_keys = {"from", "to", "amount"}
    return required_keys.issubset(transaction.keys()) and \
           validate_address(transaction["from"]) and \
           validate_address(transaction["to"]) and \
           validate_amount(transaction["amount"])


def main():
    transactions = [
        {"from": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "to": "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy", "amount": 0.01},
        {"from": "0x5B38e3156B3c499BFe8156c3BF2f1aA199D8bCD5", "to": "0x5C69bce89f43f5c8aAA889FE49F7A7cB320BA8D9", "amount": 0.1}
    ]

    for transaction in transactions:
        if validate_transaction(transaction):
            print("Valid transaction:", transaction)
        else:
            print("Invalid transaction:", transaction)


if __name__ == "__main__":
    main()