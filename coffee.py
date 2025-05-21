from order import Order

class Coffee:
    # ... (existing code)

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})




class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")


    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0
