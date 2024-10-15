from Task11.service.ICustomerServiceProvider import ICustomerServiceProvider
from Task11.service.IBankServiceProvider import IBankServiceProvider
from Task11.bean.Account import SavingsAccount, CurrentAccount, ZeroBalanceAccount

class BankServiceProviderImpl(ICustomerServiceProvider, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        self.branch_name = branch_name
        self.branch_address = branch_address
        self.account_list = []

    # Create account
    def create_account(self, customer, acc_type, balance):
        if acc_type == 'Savings':
            account = SavingsAccount(customer, balance)
        elif acc_type == 'Current':
            account = CurrentAccount(customer, balance)
        elif acc_type == 'ZeroBalance':
            account = ZeroBalanceAccount(customer, balance)
        else:
            raise ValueError("Invalid account type")
        self.account_list.append(account)
        return account.account_number

    # List all accounts
    def list_accounts(self):
        for account in self.account_list:
            account.print_account_info()

    # Get account balance
    def get_account_balance(self, account_number):
        account = self.find_account(account_number)
        return account.balance

    # Deposit
    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        return account.deposit(amount)

    # Withdraw
    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        return account.withdraw(amount)

    # Transfer
    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Transferred {amount} from {from_account_number} to {to_account_number}")

    # Get account details
    def get_account_details(self, account_number):
        account = self.find_account(account_number)
        account.print_account_info()

    # Calculate interest for all savings accounts
    def calculate_interest(self):
        for account in self.account_list:
            if isinstance(account, SavingsAccount):
                interest = account.calculate_interest()
                account.balance += interest
                print(f"Interest added to account {account.account_number}: {interest}")

    # Helper method to find an account
    def find_account(self, account_number):
        for account in self.account_list:
            if account.account_number == account_number:
                return account
        raise ValueError("Account not found")
