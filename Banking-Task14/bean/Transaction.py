class Transaction:
    def __init__(self, transaction_id, account_number, description, transaction_type, amount):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount

    def __repr__(self):
        return f"Transaction({self.transaction_id}, {self.account_number}, {self.transaction_type}, {self.amount})"
