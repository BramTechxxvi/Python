from estore.billing_information import BillingInformation
from estore.user import User


class Customer(User):

    def __init__(self, name, age, house_address, email, phone_number, password, shopping_cart, billing_info=None):
        super().__init__(name, age, house_address, email, phone_number, password)
        self.billing_info = billing_info if billing_info is None else []
        self.cart = shopping_cart()
        