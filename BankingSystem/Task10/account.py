class Account:
    _account_number_counter = 1001  # Class variable to keep track of account numbers

    def __init__(self, account_type=None, balance=0.0, customer=None):
        self.account_number = Account._account_number_counter
        Account._account_number_counter += 1  # Increment for the next account
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    # Getters and Setters
    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_balance(self):
        return self.balance

    def deposit(self, amount: float):
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def print_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        if self.customer:
            print("Customer Information:")
            self.customer.print_info()
