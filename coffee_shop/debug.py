

from customer import Customer
from coffee import Coffee


c1 = Customer("Alice")
c2 = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")


o1 = c1.create_order(latte, 4.5)
o2 = c1.create_order(mocha, 5.0)
o3 = c2.create_order(latte, 6.5)


print(f"{latte.name} orders: {latte.num_orders()}")
print(f"Alice coffees: {[c.name for c in c1.coffees()]}")
print(f"Latte average price: ${latte.average_price():.2f}")
print(f"Top aficionado for Latte: {Customer.most_aficionado(latte).name}")
