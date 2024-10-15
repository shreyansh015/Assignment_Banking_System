from Task12.bean.BankServiceProviderImpl import BankServiceProviderImpl
from Task12.bean.Customer import Customer
from Task12.bean.Account import SavingsAccount, CurrentAccount, Account
from Task12.exceptions.InsufficientFundException import InsufficientFundException
from Task12.exceptions.InvalidAccountException import InvalidAccountException
from Task12.exceptions.OverDraftLimitExceededException import OverDraftLimitExceededException

bank_service = BankServiceProviderImpl()


def main():
    while True:
        try:
            print("\nWelcome to the Bank")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Details")
            print("6. Exit")
            choice = int(input("Choose an option: "))

            if choice == 1:
                print("\n--- Create Account ---")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                address = input("Enter address: ")

                customer = Customer(
                    customer_id=len(bank_service.account_list) + 1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address=address
                )

                print("\nChoose Account Type:")
                print("1. Savings Account (min balance 500, 3% interest)")
                print("2. Current Account (overdraft limit 1000)")
                print("3. Zero Balance Account")
                account_choice = int(input("Enter account type (1/2/3): "))

                if account_choice == 1:
                    balance = float(input("Enter initial deposit (min 500): "))
                    if balance < 500:
                        print("Initial deposit must be at least 500 for Savings Account.")
                    else:
                        account = SavingsAccount(balance=balance, customer=customer)
                        bank_service.create_account(account)
                elif account_choice == 2:
                    balance = float(input("Enter initial deposit: "))
                    account = CurrentAccount(balance=balance, customer=customer)
                    bank_service.create_account(account)
                elif account_choice == 3:
                    balance = 0.0  # Zero Balance Account starts with no balance
                    account = Account(account_type="Zero Balance", balance=balance, customer=customer)
                    bank_service.create_account(account)
                else:
                    print("Invalid account type choice.")

            elif choice == 2:
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                bank_service.deposit(acc_no, amount)
            elif choice == 3:
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter withdraw amount: "))
                bank_service.withdraw(acc_no, amount)
            elif choice == 4:
                from_acc = int(input("Enter your account number: "))
                to_acc = int(input("Enter recipient's account number: "))
                amount = float(input("Enter amount to transfer: "))
                bank_service.transfer(from_acc, to_acc, amount)
            elif choice == 5:
                acc_no = int(input("Enter account number: "))
                details = bank_service.getAccountDetails(acc_no)
                print(details)
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

        except InsufficientFundException as e:
            print(e)
        except InvalidAccountException as e:
            print(e)
        except OverDraftLimitExceededException as e:
            print(e)
        except ValueError:
            print("Invalid input. Please enter the correct data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"NullPointerException occurred: {e}")
