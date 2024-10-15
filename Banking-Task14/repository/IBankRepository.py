class IBankRepository:
    def create_account(self, account_type, customer_id, initial_balance):
        raise NotImplementedError

    def get_account(self, account_number):
        raise NotImplementedError

    def update_account(self, account):
        raise NotImplementedError

    def add_transaction(self, account_number, description, amount):
        raise NotImplementedError

    def list_accounts(self, customer_id):
        raise NotImplementedError
