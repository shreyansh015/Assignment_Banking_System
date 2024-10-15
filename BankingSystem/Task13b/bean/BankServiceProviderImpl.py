# bean/BankServiceProviderImpl.py

from Task13b.bean.Account import Account, SavingsAccount, CurrentAccount
from Task13b.bean.Customer import Customer
from Task13b.service.ICustomerServiceProvider import ICustomerServiceProvider
from Task13b.service.IBankServiceProvider import IBankServiceProvider


class BankServiceProviderImpl(ICustomerServiceProvider, IBankServiceProvider):
    def __init__(self):
        self.account_set = set()  # Set to store accounts

    def create_account(self, customer: Customer, acc_type: str, balance: float):
        if acc_type == 'Savings':
            if balance < 500:
                raise ValueError("Minimum balance for savings account is 500.")
            account = SavingsAccount(customer, balance)
        elif acc_type == 'Current':
            account = CurrentAccount(customer, balance)
        else:
            raise ValueError("Invalid account type")

        if account in self.account_set:
            print(f"Account with account number {account.account_number} already exists.")
        else:
            self.account_set.add(account)
            print(
                f"Account created for {customer.first_name} {customer.last_name} with account number {account.account_number}")

    def list_accounts(self):
        print("Listing all accounts:")
        sorted_accounts = sorted(self.account_set, key=lambda acc: acc.customer.last_name)
        for account in sorted_accounts:
            print(
                f"Account No: {account.account_number}, Customer: {account.customer.first_name} {account.customer.last_name}, Balance: {account.balance}")

    def get_account_balance(self, account_number):
        for account in self.account_set:
            if account.account_number == account_number:
                return account.balance
        raise ValueError("Account not found.")

    def deposit(self, account_number, amount):
        for account in self.account_set:
            if account.account_number == account_number:
                account.deposit(amount)
                return account.balance
        raise ValueError("Account not found.")

    def withdraw(self, account_number, amount):
        for account in self.account_set:
            if account.account_number == account_number:
                account.withdraw(amount)
                return account.balance
        raise ValueError("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        to_account = None
        for account in self.account_set:
            if account.account_number == from_account_number:
                from_account = account
            if account.account_number == to_account_number:
                to_account = account

        if not from_account or not to_account:
            raise ValueError("One or both accounts not found.")

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Transferred {amount} from account {from_account_number} to {to_account_number}")

    def get_account_details(self, account_number):
        for account in self.account_set:
            if account.account_number == account_number:
                return {
                    'Account Number': account.account_number,
                    'Customer Name': f"{account.customer.first_name} {account.customer.last_name}",
                    'Balance': account.balance
                }
        raise ValueError("Account not found.")
