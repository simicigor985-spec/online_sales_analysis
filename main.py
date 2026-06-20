import random

from product import Product
from product_menager import ProductManager
from cart import Cart
manager = ProductManager()
cart = Cart()

product1 = Product("Laptop", 999.99, 10)
product2 = Product("Mouse", 29.99, 50)
product3 = Product("Keyboard", 79.99, 30)
manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.show_products()
manager.total_inventory_value()

random_product = random.sample(manager.get_products(), 3)
for product in random_product:
    cart.add_item(product, 2)
cart.show_cart_items()
