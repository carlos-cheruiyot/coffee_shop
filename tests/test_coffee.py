import pytest
from ..coffee import Coffee
from ..customer import Customer
from ..order import Order


def test_coffee_name_valid():
    coffee = Coffee("Americano")
    assert coffee.name == "Americano"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("Hi")

def test_coffee_orders_and_customers():
    coffee = Coffee("Flat White")
    c1 = Customer("Tom")
    c2 = Customer("Jerry")
    Order(c1, coffee, 5.5)
    Order(c2, coffee, 6.0)

    assert len(coffee.orders()) == 2
    assert c1 in coffee.customers()
    assert c2 in coffee.customers()

def test_coffee_aggregate_methods():
    coffee = Coffee("Cappuccino")
    c = Customer("Emma")
    c.create_order(coffee, 4.0)
    c.create_order(coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
