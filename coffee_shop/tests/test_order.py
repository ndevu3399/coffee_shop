
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def teardown_function():
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

def test_invalid_customer_type():
    coffee = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 4.0)

def test_invalid_coffee_type():
    customer = Customer("Zoe")
    with pytest.raises(TypeError):
        Order(customer, "not coffee", 4.0)

def test_price_validation():
    customer = Customer("Leo")
    coffee = Coffee("Americano")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)   
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)  
    
    o = Order(customer, coffee, 7.0)
    assert o.price == 7.0
