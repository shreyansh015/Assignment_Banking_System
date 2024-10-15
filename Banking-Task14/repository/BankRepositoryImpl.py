import sqlite3

import pyodbc

from exceptions.AccountNotFoundException import AccountNotFoundException
from repository.IBankRepository import IBankRepository
from util.DBUtil import DBUtil
from bean.Account import Account
from bean.Transaction import Transaction

class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.conn = DBUtil.get_connection()

    def create_account(self, account_type, customer_id, initial_balance):
        global cursor
        try:
            cursor = self.conn.cursor()
            # Use OUTPUT clause to get the last inserted account number
            cursor.execute("""
                INSERT INTO Accounts (account_type, balance, customer_id) 
                OUTPUT INSERTED.account_number
                VALUES (?, ?, ?)
            """, (account_type, initial_balance, customer_id))

            # Fetch the last inserted account number
            account_number = cursor.fetchone()[0]  # Get the first column of the first row
            self.conn.commit()
            return account_number
        except pyodbc.IntegrityError as e:
            # Handle integrity error (like foreign key constraint violation)
            raise AccountNotFoundException("Customer ID does not exist.") from e
        except Exception as e:
            # Handle other exceptions
            raise Exception("An error occurred while creating the account.") from e
        finally:
            cursor.close()

    def get_account(self, account_number):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Accounts WHERE account_number = ?", (account_number,))
        row = cursor.fetchone()
        if row:
            return Account(account_number=row[0], account_type=row[1], balance=row[2], customer_id=row[3])
        return None

    def update_account(self, account):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Accounts SET balance = ? WHERE account_number = ?",
                       (account.balance, account.account_number))
        self.conn.commit()

    def add_transaction(self, account_number, description, amount):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Transactions (account_number, description, transaction_type, amount) VALUES (?, ?, ?, ?)",
                       (account_number, description, 'Credit' if description == "Deposit" else 'Debit', amount))
        self.conn.commit()

    def list_accounts(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Accounts WHERE customer_id = ?", (customer_id,))
        rows = cursor.fetchall()
        return [Account(account_number=row[0], account_type=row[1], balance=row[2], customer_id=row[3]) for row in rows]

    def update_account_balance(self, account_number, new_balance):
        global cursor
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE Accounts
                SET balance = ?
                WHERE account_number = ?
            """, (new_balance, account_number))
            self.conn.commit()
        except Exception as e:
            raise Exception("An error occurred while updating the account balance.") from e
        finally:
            cursor.close()

    def get_account_by_number(self, account_number):
        global cursor
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT account_number, account_type, balance, customer_id FROM Accounts WHERE account_number = ?",
                (account_number,))
            row = cursor.fetchone()

            if row:
                return Account(account_number=row[0], account_type=row[1], balance=row[2], customer_id=row[3])
            return None  # Return None if the account is not found
        except Exception as e:
            raise Exception("An error occurred while fetching the account.") from e
        finally:
            cursor.close()

