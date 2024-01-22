from datetime import datetime
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def _repr_(self):
        return f"{self.name}: ${self.price} ({self.quantity} in stock)"

    def is_in_stock(self):
        return self.quantity > 0

    def decrease_stock(self, amount):
        self.quantity -= amount


class ShoppingCart:
    def __init__(self):
        self.items = {}
        
    def print_cart(self):
        """Prints the items in the shopping cart."""
        for item, quantity in self.items.items():
            print(f"{item.name}: {quantity} in stock")

    def add_item(self, product, quantity):
        if product.is_in_stock():
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.decrease_stock(quantity)
        else:
            print(f"Sorry, {product.name} is out of stock!")

    def remove_item(self, product, quantity):
        if product in self.items:
            if self.items[product] >= quantity:
                self.items[product] -= quantity
                if self.items[product] == 0:
                    del self.items[product]
            else:
                print(f"Insufficient quantity of {product.name} in cart!")
        else:
            print(f"{product.name} is not in your cart!")

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def _repr_(self):
        total_price = self.total_price()
        items_string = "\n".join(f"\t- {product}: {quantity} x ${product.price}" 
                            for product, quantity in self.items.items())
        return f"Cart:\n{items_string}\nTotal: ${total_price}"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.orders = []

    def login(self, password):
        return self.password == password

    def add_order(self, cart):
        order = {
            "date": datetime.now(),
            "products": [{'name': product.name, 'quantity': quantity} 
                         for product, quantity in cart.items.items()],
            "total_price": cart.total_price()
        }
        self.orders.append(order)
        cart.items.clear()

    def view_orders(self):
        for i, order in enumerate(self.orders, 1):
            print(f"Order #{i}:\n\tDate: {order['date']}\n\tProducts:")
            for product in order['products']:
                print(f"\t\t- {product['name']}: {product['quantity']}")
            print(f"\tTotal: ${order['total_price']}")


# Example usage
user = User("Lahari", "21A31A4288")
cart = ShoppingCart()

products = [
    Product("Frock", 10.99, 5),
    Product("Macbook", 599.99, 2),
    Product("violine", 15.50, 10),
]

cart.add_item(products[0], 2)
cart.add_item(products[1], 1)
cart.remove_item(products[2], 1)

print(f"Logged in as: {user.username}")
if user.login("21A31A4288"):
    cart.print_cart()
    user.add_order(cart)
    print("Order placed successfully!")
    user.view_orders()
else:
    print("Invalid password!")
