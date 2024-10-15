class Account:
    account_number_counter = 1001  # Static variable to generate unique account numbers

    def __init__(self, account_type, balance, customer):
        self.account_number = Account.account_number_counter
        Account.account_number_counter += 1
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def __str__(self):
        return f"Account [Number: {self.account_number}, Type: {self.account_type}, Balance: {self.balance}, Customer: {self.customer}]"


class SavingsAccount(Account):
    def __init__(self, balance, customer, interest_rate=0.03):
        super().__init__('Savings', balance, customer)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def __str__(self):
        return f"SavingsAccount [Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}]"


class CurrentAccount(Account):
    def __init__(self, balance, customer, overdraft_limit=1000):
        super().__init__('Current', balance, customer)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"CurrentAccount [Number: {self.account_number}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}]"
