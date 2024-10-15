from bean.Customer import Customer

class CustomerServiceProviderImpl:
    def __init__(self):
        self.customers = []
        self.customer_id_counter = 1

    def create_customer(self, first_name, last_name, email, phone, address):
        customer = Customer(self.customer_id_counter, first_name, last_name, email, phone, address)
        self.customers.append(customer)
        self.customer_id_counter += 1
        return customer

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        raise Exception("Customer Not Found")
