from bank import Bank
from customer import Customer

def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer Money")
        print("6. Get Account Details")
        print("7. Exit")

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

            acc_type = input("Enter Account Type (Savings/Current): ")
            balance = float(input("Enter Initial Balance: "))

            acc_number = bank.create_account(customer, acc_type, balance)
            print(f"Account created successfully with Account Number: {acc_number}")

        elif choice == '2':
            # Deposit into an account
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Deposit Amount: "))
            new_balance = bank.deposit(account_number, amount)
            print(f"Deposited {amount}. New Balance: {new_balance}")

        elif choice == '3':
            # Withdraw from an account
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Withdrawal Amount: "))
            try:
                new_balance = bank.withdraw(account_number, amount)
                print(f"Withdrew {amount}. New Balance: {new_balance}")
            except ValueError as e:
                print(e)

        elif choice == '4':
            # Get account balance
            account_number = int(input("Enter Account Number: "))
            try:
                balance = bank.get_account_balance(account_number)
                print(f"Account Balance: {balance}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            # Transfer money between accounts
            from_account_number = int(input("Enter From Account Number: "))
            to_account_number = int(input("Enter To Account Number: "))
            amount = float(input("Enter Amount to Transfer: "))
            try:
                bank.transfer(from_account_number, to_account_number, amount)
            except ValueError as e:
                print(e)

        elif choice == '6':
            # Get account details
            account_number = int(input("Enter Account Number: "))
            try:
                bank.get_account_details(account_number)
            except ValueError as e:
                print(e)

        elif choice == '7':
            print("Exiting the Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
