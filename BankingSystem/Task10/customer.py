import re

class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    # Getters and Setters
    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        if self.validate_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email address.")

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        if self.validate_phone(phone):
            self.phone = phone
        else:
            raise ValueError("Invalid phone number.")

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    # Validation methods
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

    # Print customer info
    def print_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
