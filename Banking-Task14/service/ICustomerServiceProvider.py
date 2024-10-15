from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):
    @abstractmethod
    def create_customer(self, first_name, last_name, email, phone, address):
        pass

    @abstractmethod
    def get_customer(self, customer_id):
        pass
