"""
Coffee Class Module

This module defines the Coffee class for the Coffee Shop system.
A Coffee represents a type of coffee that can be ordered by customers.

Key Features:
- Name validation (minimum 3 characters, string only)
- Immutable name property (cannot be changed after creation)
- Relationship management with orders and customers
- Aggregate calculations (order count, average price)
- Bonus: most_aficionado class method
"""

class Coffee:
    """
    Represents a type of coffee in the coffee shop system.

    A coffee has an immutable name and tracks all orders placed for it.
    Provides methods to analyze sales data and customer behavior.

    Attributes:
        name (str): The coffee's name (immutable, min 3 characters)
        _orders (list): Private list of Order objects for this coffee

    Relationships:
        - One-to-many with Order (a coffee can have multiple orders)
        - Many-to-many with Customer (through orders)

    Business Logic:
        - Name cannot be changed after creation (immutable)
        - Tracks all orders and customers automatically
        - Provides sales analytics methods
    """

    def __init__(self, name):
        """
        Initialize a new Coffee instance.

        Args:
            name (str): The coffee's name (must be at least 3 characters)

        Raises:
            ValueError: If name is not a string or less than 3 characters

        Example:
            latte = Coffee("Latte")  # Creates coffee named "Latte"
        """
        self.name = name
        self._orders = []

    @property
    def name(self):
        """
        Get the coffee's name.

        Returns:
            str: The coffee's immutable name

        Example:
            coffee_name = coffee.name  # Returns "Latte"
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the coffee's name with validation (only during initialization).

        This setter prevents changing the name after the coffee object is created,
        making the name truly immutable.

        Args:
            value (str): The coffee's name

        Raises:
            ValueError: If name is not a string, too short, or if trying to change existing name

        Example:
            # This works during initialization:
            coffee = Coffee("Espresso")

            # This will raise an error:
            coffee.name = "Cappuccino"  # ValueError!
        """
        if hasattr(self, '_name'):
            raise ValueError("Coffee name is immutable and cannot be changed")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value

    def orders(self):
        """
        Get all orders placed for this coffee.

        Returns:
            list: List of Order objects for this coffee

        Example:
            coffee_orders = coffee.orders()  # Returns all orders for this coffee
        """
        return self._orders

    def customers(self):
        """
        Get all unique customers who have ordered this coffee.

        Returns:
            list: List of unique Customer objects who ordered this coffee

        Example:
            coffee_customers = coffee.customers()  # Returns all customers who ordered this coffee
        """
        return list(set([order.customer for order in self._orders]))

    def num_orders(self):
        """
        Get the total number of orders placed for this coffee.

        Returns:
            int: Total number of orders for this coffee

        Example:
            order_count = coffee.num_orders()  # Returns total orders
        """
        return len(self._orders)

    def average_price(self):
        """
        Calculate the average price of all orders for this coffee.

        Returns:
            float: Average price of orders, or 0 if no orders exist

        Example:
            avg_price = coffee.average_price()  # Returns average price
        """
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Find the customer who has spent the most money on a given coffee.

        This is a bonus method that analyzes spending patterns to identify
        the most dedicated customer for a particular coffee type.

        Args:
            coffee (Coffee): The coffee to analyze

        Returns:
            Customer or None: The customer who spent the most on this coffee,
                            or None if no orders exist

        Example:
            top_customer = Coffee.most_aficionado(latte)  # Returns top spender for latte
        """
        if not coffee._orders:
            return None

        customers = coffee.customers()
        if not customers:
            return None

        # Find customer who spent the most on this coffee
        max_spent = 0
        most_aficionado_customer = None

        for customer in customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                most_aficionado_customer = customer

        return most_aficionado_customer
