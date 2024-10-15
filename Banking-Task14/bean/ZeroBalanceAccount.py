from bean.Account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, account_number, customer_id):
        super().__init__(account_number, "Zero Balance", 0.0, customer_id)
