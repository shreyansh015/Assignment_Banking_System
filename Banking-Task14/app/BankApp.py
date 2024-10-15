from service.BankServiceProviderImpl import BankServiceProviderImpl
from exceptions import AccountNotFoundException, InsufficientFundsException

def main():
    bank_service = BankServiceProviderImpl()
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. List Accounts")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_type = input("Enter account type (Savings/Current): ")
            customer_id = int(input("Enter customer ID: "))
            initial_balance = float(input("Enter initial balance: "))
            account_number = bank_service.create_account(account_type, customer_id, initial_balance)
            print(f"Account created successfully. Account Number: {account_number}")

        elif choice == '2':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            new_balance = bank_service.deposit(account_number, amount)
            print(f"Deposit successful. New Balance: {new_balance}")

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            try:
                new_balance = bank_service.withdraw(account_number, amount)
                print(f"Withdrawal successful. New Balance: {new_balance}")
            except InsufficientFundsException as e:
                print(e)

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            try:
                balance = bank_service.get_balance(account_number)
                print(f"Balance: {balance}")
            except AccountNotFoundException as e:
                print(e)

        elif choice == '5':
            from_account = int(input("Enter source account number: "))
            to_account = int(input("Enter target account number: "))
            amount = float(input("Enter transfer amount: "))
            try:
                bank_service.transfer(from_account, to_account, amount)
                print("Transfer successful.")
            except (AccountNotFoundException, InsufficientFundsException) as e:
                print(e)

        elif choice == '6':
            account_number = int(input("Enter account number: "))
            try:
                account_details = bank_service.get_account_details(account_number)
                print(account_details)
            except AccountNotFoundException as e:
                print(e)

        elif choice == '7':
            customer_id = int(input("Enter customer ID: "))
            accounts = bank_service.list_accounts(customer_id)
            if accounts:
                for account in accounts:
                    print(account)
            else:
                print("No accounts found for this customer.")

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
