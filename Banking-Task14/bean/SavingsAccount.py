from bean.Account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance, customer_id):
        super().__init__(account_number, "Savings", balance, customer_id)
