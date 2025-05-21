import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization_valid():
    c = Customer("Max")
    coffee = Coffee("Latte")
    order = Order(c, coffee, 4.5)

    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.5

def test_order_invalid_price():
    c = Customer("Lily")
    coffee = Coffee("Cortado")
    
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)

    with pytest.raises(ValueError):
        Order(c, coffee, 11.0)

def test_order_invalid_types():
    with pytest.raises(ValueError):
        Order("NotCustomer", Coffee("Macchiato"), 3.5)

    with pytest.raises(ValueError):
        Order(Customer("Real"), "NotCoffee", 3.5)
