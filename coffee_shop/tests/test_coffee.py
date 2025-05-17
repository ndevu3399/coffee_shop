
import pytest
from coffee import Coffee
from customer import Customer

def teardown_function():
    Coffee.all_coffees.clear()
    Customer.all_customers.clear()
    

def test_name_validation():
    with pytest.raises(ValueError):
        Coffee("AB")   

def test_orders_and_customers_and_aggregates():
    c1 = Customer("Amy")
    c2 = Customer("Eli")
    coffee = Coffee("Latte")
    o1 = c1.create_order(coffee, 3.0)
    o2 = c2.create_order(coffee, 5.0)
    
    assert coffee.orders() == [o1, o2]
    
    assert set(coffee.customers()) == {c1, c2}
    
    assert coffee.num_orders() == 2
    
    assert coffee.average_price() == pytest.approx((3.0 + 5.0) / 2)
