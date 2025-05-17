
from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        """Return a list of all orders placed by this customer."""
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        """Return a unique list of Coffees this customer has ordered."""
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        """Create a new Order for this customer."""
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Return the Customer who has spent the most on the given Coffee.
        If no orders for that coffee exist, returns None.
        """
        totals = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                totals[order.customer] = totals.get(order.customer, 0.0) + order.price
        if not totals:
            return None
        return max(totals, key=totals.get)
