import pyodbc

class DBUtil:
    @staticmethod
    def get_connection():
        # Define your database connection parameters here
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=BankDB;Trusted_Connection=yes;'
        try:
            conn = pyodbc.connect(conn_string)
            return conn
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            return None
