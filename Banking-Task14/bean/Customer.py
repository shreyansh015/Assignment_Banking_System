class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.first_name}, {self.last_name})"
