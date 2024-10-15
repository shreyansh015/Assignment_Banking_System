# bean/Account.py

class Account:
    last_acc_no = 1000

    def __init__(self, customer, balance):
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def __eq__(self, other):
        return self.account_number == other.account_number

    def __hash__(self):
        return hash(self.account_number)

    def __repr__(self):
        return f"Account({self.account_number}, {self.customer.first_name} {self.customer.last_name}, Balance: {self.balance})"

class SavingsAccount(Account):
    def __init__(self, customer, balance):
        if balance < 500:
            raise ValueError("Minimum balance for savings account is 500")
        super().__init__(customer, balance)

class CurrentAccount(Account):
    def __init__(self, customer, balance, overdraft_limit=1000):
        super().__init__(customer, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            raise ValueError("Overdraft limit exceeded")
