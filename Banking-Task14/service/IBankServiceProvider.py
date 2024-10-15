# service/IBankServiceProvider.py
class IBankServiceProvider:
    def create_account(self, account_type, customer_id, initial_balance):
        raise NotImplementedError

    def deposit(self, account_number, amount):
        raise NotImplementedError

    def withdraw(self, account_number, amount):
        raise NotImplementedError

    def get_balance(self, account_number):
        raise NotImplementedError

    def transfer(self, from_account, to_account, amount):
        raise NotImplementedError

    def get_account_details(self, account_number):
        raise NotImplementedError

    def list_accounts(self, customer_id):
        raise NotImplementedError
