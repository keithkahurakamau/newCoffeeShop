import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_order_init(self):
        customer = Customer("John")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.5)

        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.5

    def test_order_price_validation(self):
        customer = Customer("John")
        coffee = Coffee("Latte")

        with pytest.raises(Exception):
            Order(customer, coffee, 0.5)  # too low

        with pytest.raises(Exception):
            Order(customer, coffee, 15.0)  # too high

        with pytest.raises(Exception):
            Order(customer, coffee, "4.5")  # not a float

    def test_order_price_immutable(self):
        customer = Customer("John")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.5)

        with pytest.raises(Exception):
            order.price = 5.0

    def test_order_customer_validation(self):
        coffee = Coffee("Latte")
        with pytest.raises(ValueError):
            Order("John", coffee, 4.5)  # not a Customer instance

    def test_order_coffee_validation(self):
        customer = Customer("John")
        with pytest.raises(ValueError):
            Order(customer, "Latte", 4.5)  # not a Coffee instance
