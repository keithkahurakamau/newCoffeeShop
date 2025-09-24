# Coffee Shop Management System

A Python-based coffee shop management system that tracks customers, coffee types, and orders with comprehensive analytics and validation features.

## Features

- **Coffee Management**: Create and manage different coffee types with immutable names and sales tracking
- **Customer Management**: Handle customer information with validation and order history
- **Order Processing**: Create orders linking customers to coffees with price validation
- **Analytics**: Calculate order counts, average prices, and identify top customers
- **Data Validation**: Comprehensive validation for names, prices, and object types
- **Relationship Management**: Automatic handling of many-to-many relationships between customers and coffees

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd newCoffeeShop
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

### Coffee Class

The `Coffee` class represents different types of coffee available in the shop.

```python
from coffee import Coffee

# Create a new coffee type
latte = Coffee("Latte")

# Get coffee information
print(latte.name)  # Output: Latte
print(latte.num_orders())  # Output: 0

# Analytics
latte_orders = latte.orders()
latte_customers = latte.customers()
avg_price = latte.average_price()
```

### Customer Class

The `Customer` class manages customer information and their orders.

```python
from customer import Customer

# Create a new customer
customer = Customer("John Doe")

# Update customer name
customer.name = "Jane Doe"

# Get customer data
orders = customer.orders()
coffees = customer.coffees()
```

### Order Class

The `Order` class handles the relationship between customers and coffees.

```python
from order import Order
from coffee import Coffee
from customer import Customer

# Create objects
customer = Customer("Alice")
coffee = Coffee("Espresso")

# Create an order
order = Order(customer, coffee, 3.50)

# Order automatically adds itself to customer and coffee
print(len(customer.orders()))  # Output: 1
print(len(coffee.orders()))    # Output: 1
print(order.price)             # Output: 3.5
```

### Advanced Features

#### Finding Top Customers

Use the `most_aficionado` class method to find the customer who spends the most on a particular coffee:

```python
from coffee import Coffee

# Find the customer who spends the most on a specific coffee
top_customer = Coffee.most_aficionado(coffee)
if top_customer:
    print(f"Top customer: {top_customer.name}")
```

## Project Structure

```
newCoffeeShop/
├── coffee.py          # Coffee class implementation
├── customer.py        # Customer class implementation
├── order.py           # Order class implementation
├── tests/             # Test files
│   ├── test_coffee.py
│   ├── test_customer.py
│   └── test_order.py
├── requirements.txt   # Python dependencies
├── LICENSE            # MIT License
└── README.md          # This file
```

## Testing

The project includes comprehensive tests using pytest. To run the tests:

```bash
# Run all tests
pytest

# Run tests for a specific class
pytest tests/test_coffee.py
pytest tests/test_customer.py
pytest tests/test_order.py

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=html
```

## Dependencies

- **pytest**: Testing framework
- **colorama**: Cross-platform colored terminal text
- **Pygments**: Syntax highlighting for test output
- **pluggy**: Pytest plugin for better reporting
- **packaging**: Python packaging utilities
- **iniconfig**: Configuration file parsing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## Support

For questions or issues, please open an issue on the repository or contact the maintainers.
