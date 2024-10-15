# app/BankApp.py

from Task13a.bean.BankServiceProviderImpl import BankServiceProviderImpl
from Task13a.bean.Customer import Customer

bank_service = BankServiceProviderImpl()


def main():
    while True:
        print("\nWelcome to the Bank")
        print("1. Create Account")
        print("2. List Accounts")
        print("3. Get Account Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Get Account Details")
        print("8. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            acc_type = input("Enter account type (Savings/Current): ")
            balance = float(input("Enter initial balance: "))
            customer = Customer(first_name, last_name, email, phone)
            bank_service.create_account(customer, acc_type, balance)

        elif choice == 2:
            bank_service.list_accounts()

        elif choice == 3:
            acc_no = int(input("Enter account number: "))
            print("Balance: ", bank_service.get_account_balance(acc_no))

        elif choice == 4:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            print("New Balance: ", bank_service.deposit(acc_no, amount))

        elif choice == 5:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            print("New Balance: ", bank_service.withdraw(acc_no, amount))

        elif choice == 6:
            from_acc = int(input("Enter your account number: "))
            to_acc = int(input("Enter recipient's account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank_service.transfer(from_acc, to_acc, amount)

        elif choice == 7:
            acc_no = int(input("Enter account number: "))
            details = bank_service.get_account_details(acc_no)
            print(details)

        elif choice == 8:
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
