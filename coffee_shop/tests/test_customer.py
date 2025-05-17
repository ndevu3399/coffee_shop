
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def teardown_function():
    
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

def test_name_validation():
    with pytest.raises(ValueError):
        Customer("")             
    with pytest.raises(ValueError):
        Customer("x" * 16)       

def test_create_order_and_relations():
    c = Customer("Dan")
    coffee = Coffee("Espresso")
    order = c.create_order(coffee, 3.5)
    assert order in Order.all_orders
    assert order.customer is c
    assert order.coffee is coffee

    
    assert c.orders() == [order]
    assert c.coffees() == [coffee]

def test_most_aficionado():
    c1 = Customer("Ann")
    c2 = Customer("Ben")
    coffee = Coffee("Cappuccino")
    c1.create_order(coffee, 4.0)
    c1.create_order(coffee, 2.0)
    c2.create_order(coffee, 7.0)
    
    assert Customer.most_aficionado(coffee) is c2

def test_most_aficionado_no_orders():
    coffee = Coffee("Drip")
    assert Customer.most_aficionado(coffee) is None
