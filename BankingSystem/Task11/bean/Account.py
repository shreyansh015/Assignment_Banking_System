from abc import ABC, abstractmethod

class Account(ABC):
    lastAccNo = 1000  # Static variable for unique account numbers

    def __init__(self, account_type, customer, balance=0.0):
        self.account_number = Account.lastAccNo + 1
        Account.lastAccNo += 1
        self.account_type = account_type
        self.customer = customer
        self.balance = balance

    # Abstract method to calculate interest
    @abstractmethod
    def calculate_interest(self):
        pass

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # Withdraw method
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Print account details
    def print_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        self.customer.print_info()

# Savings Account with minimum balance and interest rate
class SavingsAccount(Account):
    def __init__(self, customer, balance=500):
        if balance < 500:
            raise ValueError("Savings Account requires a minimum balance of 500.")
        super().__init__('Savings', customer, balance)
        self.interest_rate = 0.03  # 3% interest rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def withdraw(self, amount):
        if self.balance - amount < 500:
            raise ValueError("Cannot withdraw, minimum balance of 500 required.")
        self.balance -= amount
        return self.balance

# Current Account with overdraft limit
class CurrentAccount(Account):
    def __init__(self, customer, balance=0.0):
        super().__init__('Current', customer, balance)
        self.overdraft_limit = 1000

    def calculate_interest(self):
        return 0  # No interest on current account

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
        return self.balance

# Zero Balance Account with no minimum balance requirement
class ZeroBalanceAccount(Account):
    def __init__(self, customer, balance=0.0):
        super().__init__('ZeroBalance', customer, balance)

    def calculate_interest(self):
        return 0  # No interest on ZeroBalance account

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance
