from Task11.bean.BankServiceProviderImpl import BankServiceProviderImpl
from Task11.bean.Customer import Customer

def main():
    bank_service = BankServiceProviderImpl(branch_name="Main Branch", branch_address="123 Main St")

    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. List Accounts")
        print("8. Calculate Interest")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Create a new customer and account
            customer_id = input("Enter Customer ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email Address: ")
            phone = input("Enter Phone Number: ")
            address = input("Enter Address: ")

            customer = Customer(customer_id, first_name, last_name, email, phone, address)

            acc_type = input("Enter Account Type (Savings/Current/ZeroBalance): ")
            balance = float(input("Enter Initial Balance: "))

            try:
                acc_number = bank_service.create_account(customer, acc_type, balance)
                print(f"Account created successfully with Account Number: {acc_number}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Deposit Amount: "))
            try:
                new_balance = bank_service.deposit(account_number, amount)
                print(f"Deposited {amount}. New Balance: {new_balance}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Withdrawal Amount: "))
            try:
                new_balance = bank_service.withdraw(account_number, amount)
                print(f"Withdrawn {amount}. New Balance: {new_balance}")
            except ValueError as e:
                print(e)

        elif choice == '4':
            account_number = int(input("Enter Account Number: "))
            try:
                balance = bank_service.get_account_balance(account_number)
                print(f"Current Balance: {balance}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            from_account = int(input("Enter From Account Number: "))
            to_account = int(input("Enter To Account Number: "))
            amount = float(input("Enter Transfer Amount: "))
            try:
                bank_service.transfer(from_account, to_account, amount)
            except ValueError as e:
                print(e)

        elif choice == '6':
            account_number = int(input("Enter Account Number: "))
            try:
                bank_service.get_account_details(account_number)
            except ValueError as e:
                print(e)

        elif choice == '7':
            bank_service.list_accounts()

        elif choice == '8':
            bank_service.calculate_interest()

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
