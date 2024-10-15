# service/BankServiceProviderImpl.py
from repository.BankRepositoryImpl import BankRepositoryImpl
from exceptions import InsufficientFundsException, AccountNotFoundException
from service.IBankServiceProvider import IBankServiceProvider
from exceptions import AccountNotFoundException
from exceptions import CustomerNotFoundException
from exceptions import InsufficientFundsException
from decimal import Decimal
from exceptions import AccountNotFoundException

class BankServiceProviderImpl(IBankServiceProvider):
    def __init__(self):
        self.repository = BankRepositoryImpl()


    def create_account(self, account_type, customer_id, initial_balance):
        return self.repository.create_account(account_type, customer_id, initial_balance)

    def deposit(self, account_number, amount):
        try:
            # Convert the amount to Decimal to match the account balance type
            amount_decimal = Decimal(amount)
            account = self.repository.get_account_by_number(account_number)

            if account is None:
                raise AccountNotFoundException

            # Update the account balance
            account.balance += amount_decimal

            # Save the updated balance to the database
            self.repository.update_account_balance(account_number, account.balance)
            return account.balance
        except Exception as e:
            raise Exception("An error occurred while depositing funds.") from e

    def withdraw(self, account_number, amount):
        account = self.repository.get_account_by_number(account_number)
        if account is None:
            raise AccountNotFoundException

        amount = Decimal(amount)  # Convert the amount to Decimal
        if account.balance < amount:
            raise InsufficientFundsException

        account.balance -= amount
        self.repository.update_account_balance(account_number, account.balance)
        return account.balance

    def get_balance(self, account_number):
        account = self.repository.get_account(account_number)
        if account:
            return account.balance
        else:
            raise AccountNotFoundException

    def transfer(self, from_account, to_account, amount):
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)

    def get_account_details(self, account_number):
        return self.repository.get_account(account_number)

    def list_accounts(self, customer_id):
        return self.repository.list_accounts(customer_id)
