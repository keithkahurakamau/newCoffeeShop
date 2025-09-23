"""
Order Class Module

This module defines the Order class for the Coffee Shop system.
An Order represents the relationship between a Customer and a Coffee at a specific price.

Key Features:
- Price validation (1.0-10.0, float only)
- Immutable price property (cannot be changed after creation)
- Automatic relationship management (adds itself to customer and coffee)
- Type validation for customer and coffee objects
"""

class Order:
    """
    Represents an order in the coffee shop system.

    An Order is the central connecting class that links a specific Customer
    to a specific Coffee at a specific price. It automatically manages
    the relationships between customers and coffees.

    Attributes:
        customer (Customer): The customer who placed the order
        coffee (Coffee): The coffee that was ordered
        price (float): The price of the order (1.0-10.0, immutable)

    Relationships:
        - Many-to-one with Customer (many orders can belong to one customer)
        - Many-to-one with Coffee (many orders can be for one coffee type)
        - Acts as the "join table" for the many-to-many relationship

    Business Logic:
        - Price cannot be changed after creation (immutable)
        - Automatically adds itself to customer and coffee order lists
        - Validates that customer and coffee are correct types
    """

    def __init__(self, customer, coffee, price):
        """
        Initialize a new Order instance.

        Creates an order and automatically establishes relationships
        with the customer and coffee objects.

        Args:
            customer (Customer): The customer placing the order
            coffee (Coffee): The coffee being ordered
            price (float): The price of the order (1.0-10.0)

        Raises:
            ValueError: If price is invalid or customer/coffee are wrong types

        Example:
            order = Order(customer, coffee, 4.5)  # Creates order and links relationships
        """
        self.customer = customer
        self.coffee = coffee
        self.price = price

        # Add this order to both customer and coffee
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def price(self):
        """
        Get the order's price.

        Returns:
            float: The immutable price of the order

        Example:
            order_price = order.price  # Returns 4.5
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Set the order's price with validation (only during initialization).

        This setter prevents changing the price after the order is created,
        making the price truly immutable.

        Args:
            value (float): The price of the order

        Raises:
            ValueError: If value is not a float, out of range, or if trying to change existing price

        Example:
            # This works during initialization:
            order = Order(customer, coffee, 4.5)

            # This will raise an error:
            order.price = 5.0  # ValueError!
        """
        if hasattr(self, '_price'):
            raise Exception("Order price is immutable and cannot be changed")
        if not isinstance(value, float):
            raise Exception("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise Exception("Price must be between 1.0 and 10.0")
        self._price = value

    @property
    def customer(self):
        """
        Get the customer who placed this order.

        Returns:
            Customer: The customer object associated with this order

        Example:
            order_customer = order.customer  # Returns customer object
        """
        return self._customer

    @customer.setter
    def customer(self, value):
        """
        Set the customer for this order with type validation.

        Args:
            value (Customer): The customer placing the order

        Raises:
            ValueError: If value is not a Customer instance

        Example:
            order.customer = customer  # Sets customer (with validation)
        """
        # Import here to avoid circular imports
        from customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        """
        Get the coffee for this order.

        Returns:
            Coffee: The coffee object associated with this order

        Example:
            order_coffee = order.coffee  # Returns coffee object
        """
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        """
        Set the coffee for this order with type validation.

        Args:
            value (Coffee): The coffee being ordered

        Raises:
            ValueError: If value is not a Coffee instance

        Example:
            order.coffee = coffee  # Sets coffee (with validation)
        """
        # Import here to avoid circular imports
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        self._coffee = value
