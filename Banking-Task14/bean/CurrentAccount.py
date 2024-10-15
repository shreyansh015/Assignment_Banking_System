from bean.Account import Account

class CurrentAccount(Account):
    def __init__(self, account_number, balance, customer_id):
        super().__init__(account_number, "Current", balance, customer_id)
