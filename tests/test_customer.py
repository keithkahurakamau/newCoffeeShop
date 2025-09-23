import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_init(self):
        customer = Customer("John")
        assert customer.name == "John"

    def test_customer_name_validation(self):
        with pytest.raises(ValueError):
            Customer("")

        with pytest.raises(ValueError):
            Customer("A" * 16)

        with pytest.raises(ValueError):
            Customer(123)

    def test_customer_name_setter(self):
        customer = Customer("John")
        customer.name = "Jane"
        assert customer.name == "Jane"

    def test_customer_orders(self):
        customer = Customer("John")
        assert customer.orders() == []

    def test_customer_coffees(self):
        customer = Customer("John")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        Order(customer, coffee1, 4.5)
        Order(customer, coffee2, 3.0)
        Order(customer, coffee1, 4.5)  # duplicate coffee

        coffees = customer.coffees()
        assert len(coffees) == 2
        assert coffee1 in coffees
        assert coffee2 in coffees

    def test_create_order(self):
        customer = Customer("John")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 4.5)

        assert isinstance(order, Order)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.5
        assert order in customer.orders()
        assert order in coffee.orders()
