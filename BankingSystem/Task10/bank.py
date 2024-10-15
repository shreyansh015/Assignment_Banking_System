from account import Account
from customer import Customer

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer, acc_type, balance):
        account = Account(account_type=acc_type, balance=balance, customer=customer)
        self.accounts[account.get_account_number()] = account
        return account.get_account_number()

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            raise ValueError("Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        else:
            raise ValueError("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        else:
            raise ValueError("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            self.withdraw(from_account_number, amount)
            self.deposit(to_account_number, amount)
            print(f"Transferred {amount} from Account {from_account_number} to Account {to_account_number}")
        else:
            raise ValueError("One or both accounts not found.")

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            self.accounts[account_number].print_account_info()
        else:
            raise ValueError("Account not found.")
