"""
Customer Class Module

This module defines the Customer class for the Coffee Shop system.
A Customer represents a person who can place orders for coffee.

Key Features:
- Name validation (1-15 characters, string only)
- Mutable name property with validation
- Relationship management with orders and coffees
- Order creation functionality
"""

class Customer:
    """
    Represents a customer in the coffee shop system.

    A customer has a name and can place orders for different coffees.
    The customer's name is mutable but must follow validation rules.

    Attributes:
        name (str): The customer's name (1-15 characters)
        _orders (list): Private list of Order objects associated with this customer

    Relationships:
        - One-to-many with Order (a customer can have multiple orders)
        - Many-to-many with Coffee (through orders)
    """

    def __init__(self, name):
        """
        Initialize a new Customer instance.

        Args:
            name (str): The customer's name

        Raises:
            ValueError: If name is not a string or not 1-15 characters

        Example:
            customer = Customer("John")  # Creates customer named "John"
        """
        self.name = name
        self._orders = []

    @property
    def name(self):
        """
        Get the customer's name.

        Returns:
            str: The customer's current name

        Example:
            name = customer.name  # Returns "John"
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the customer's name with validation.

        Args:
            value (str): The new name

        Raises:
            ValueError: If value is not a string or not 1-15 characters

        Example:
            customer.name = "Jane"  # Changes name to "Jane"
        """
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value
        
        if value is None or value.strip() == "":
            raise Exception("Name cannot be empty or null")
        if not value.strip():
            raise Exception("Name cannot be empty or just whitespace")
        if value.isdigit():
            raise Exception("Name cannot be purely numeric")
        

    def orders(self):
        """
        Get all orders placed by this customer.

        Returns:
            list: List of Order objects belonging to this customer

        Example:
            customer_orders = customer.orders()  # Returns all customer's orders
        """
        return self._orders

    def coffees(self):
        """
        Get all unique coffees ordered by this customer.

        Returns:
            list: List of unique Coffee objects ordered by this customer

        Example:
            unique_coffees = customer.coffees()  # Returns unique coffees ordered
        """
        return list(set([order.coffee for order in self._orders]))

    def create_order(self, coffee, price):
        """
        Create a new order for this customer.

        This method creates a new Order instance and automatically
        establishes the relationships between customer, coffee, and order.

        Args:
            coffee (Coffee): The coffee being ordered
            price (float): The price of the order (1.0-10.0)

        Returns:
            Order: The newly created order instance

        Example:
            order = customer.create_order(coffee, 4.5)  # Creates new order
        """
        # Import here to avoid circular imports
        from order import Order
        order = Order(self, coffee, price)
        # Note: Order automatically adds itself to customer and coffee lists
        return order
