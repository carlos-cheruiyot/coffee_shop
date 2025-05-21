
from order import Order

class Customer:
    # ... (existing code)

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})



class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")



    def create_order(self, coffee, price):
        return Order(self, coffee, price)


    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        max_spent = 0.0
        for customer in cls.all_customers:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > max_spent:
                max_spent = total
                top_customer = customer
        return top_customer
