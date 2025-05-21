import pytest
from ..customer import Customer
from ..coffee import Coffee
from ..order import Order


def test_customer_name_valid():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_customer_name_invalid():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("A" * 20)

def test_customer_orders_and_coffees():
    c = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    c.create_order(coffee1, 5.0)
    c.create_order(coffee2, 6.0)

    assert len(c.orders()) == 2
    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()

def test_customer_most_aficionado():
    c1 = Customer("John")
    c2 = Customer("Jane")
    coffee = Coffee("Mocha")
    c1.create_order(coffee, 5.0)
    c1.create_order(coffee, 4.0)
    c2.create_order(coffee, 6.0)

    assert Customer.most_aficionado(coffee) == c1
