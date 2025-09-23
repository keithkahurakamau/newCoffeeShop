import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_coffee_init(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"

    def test_coffee_name_validation(self):
        with pytest.raises(ValueError):
            Coffee("")

        with pytest.raises(ValueError):
            Coffee("AB")  # too short

        with pytest.raises(ValueError):
            Coffee(123)

    def test_coffee_name_immutable(self):
        coffee = Coffee("Latte")
        with pytest.raises(ValueError):
            coffee.name = "Espresso"

    def test_coffee_orders(self):
        coffee = Coffee("Latte")
        assert coffee.orders() == []

    def test_coffee_customers(self):
        coffee = Coffee("Latte")
        customer1 = Customer("John")
        customer2 = Customer("Jane")
        Order(customer1, coffee, 4.5)
        Order(customer2, coffee, 3.0)
        Order(customer1, coffee, 4.5)  # duplicate customer

        customers = coffee.customers()
        assert len(customers) == 2
        assert customer1 in customers
        assert customer2 in customers

    def test_num_orders(self):
        coffee = Coffee("Latte")
        customer = Customer("John")
        Order(customer, coffee, 4.5)
        Order(customer, coffee, 3.0)

        assert coffee.num_orders() == 2

    def test_average_price(self):
        coffee = Coffee("Latte")
        customer = Customer("John")
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)

        assert coffee.average_price() == 5.0

    def test_average_price_no_orders(self):
        coffee = Coffee("Latte")
        assert coffee.average_price() == 0
