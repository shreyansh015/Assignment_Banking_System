-- Create the BankDB database
-- Create database and tables
CREATE DATABASE BankDB;

USE BankDB;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY IDENTITY(1,1), -- Start at 1, increment by 1
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255)
);


CREATE TABLE Accounts (
    account_number INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
    account_type VARCHAR(50),
    balance DECIMAL(10, 2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) -- Foreign key reference to Customers
);

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
    account_number INT,
    description VARCHAR(255),
    transaction_type VARCHAR(50),
    amount DECIMAL(10, 2),
    transaction_date DATETIME DEFAULT GETDATE(), -- Default to the current date and time
    FOREIGN KEY (account_number) REFERENCES Accounts(account_number) -- Foreign key reference to Accounts
);

INSERT INTO Customers (first_name, last_name, email, phone, address) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', '2345678901', '456 Elm St, Springfield'),
('Alice', 'Johnson', 'alice.johnson@example.com', '3456789012', '789 Maple St, Springfield'),
('Bob', 'Brown', 'bob.brown@example.com', '4567890123', '101 Oak St, Springfield'),
('Charlie', 'Davis', 'charlie.davis@example.com', '5678901234', '202 Pine St, Springfield'),
('Eve', 'White', 'eve.white@example.com', '6789012345', '303 Cedar St, Springfield');


SELECT * FROM Customers
SELECT * FROM Transactions
SELECT * FROM Accounts