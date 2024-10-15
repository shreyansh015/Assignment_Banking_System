# bean/BankServiceProviderImpl.py

# bean/BankServiceProviderImpl.py

from Task13c.bean.Account import Account, SavingsAccount, CurrentAccount
from Task13c.bean.Customer import Customer
from Task13c.service.ICustomerServiceProvider import ICustomerServiceProvider
from Task13c.service.IBankServiceProvider import IBankServiceProvider


class BankServiceProviderImpl(ICustomerServiceProvider, IBankServiceProvider):
    def __init__(self):
        self.accounts_map = {}  # Dictionary (HashMap) to store accounts

    def create_account(self, customer: Customer, acc_type: str, balance: float):
        if acc_type == 'Savings':
            if balance < 500:
                raise ValueError("Minimum balance for savings account is 500.")
            account = SavingsAccount(customer, balance)
        elif acc_type == 'Current':
            account = CurrentAccount(customer, balance)
        else:
            raise ValueError("Invalid account type")

        if account.account_number in self.accounts_map:
            print(f"Account with account number {account.account_number} already exists.")
        else:
            self.accounts_map[account.account_number] = account
            print(
                f"Account created for {customer.first_name} {customer.last_name} with account number {account.account_number}")

    def list_accounts(self):
        print("Listing all accounts:")
        sorted_accounts = sorted(self.accounts_map.values(), key=lambda acc: acc.customer.last_name)
        for account in sorted_accounts:
            print(
                f"Account No: {account.account_number}, Customer: {account.customer.first_name} {account.customer.last_name}, Balance: {account.balance}")

    def get_account_balance(self, account_number):
        account = self.accounts_map.get(account_number)
        if account:
            return account.balance
        else:
            raise ValueError("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts_map.get(account_number)
        if account:
            account.deposit(amount)
            return account.balance
        else:
            raise ValueError("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts_map.get(account_number)
        if account:
            account.withdraw(amount)
            return account.balance
        else:
            raise ValueError("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts_map.get(from_account_number)
        to_account = self.accounts_map.get(to_account_number)

        if not from_account or not to_account:
            raise ValueError("One or both accounts not found.")

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Transferred {amount} from account {from_account_number} to {to_account_number}")

    def get_account_details(self, account_number):
        account = self.accounts_map.get(account_number)
        if account:
            return {
                'Account Number': account.account_number,
                'Customer Name': f"{account.customer.first_name} {account.customer.last_name}",
                'Balance': account.balance
            }
        else:
            raise ValueError("Account not found.")
