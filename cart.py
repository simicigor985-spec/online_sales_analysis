class Cart:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        print(f"Added {quantity} of {product.name} to cart.")

    def total_cart_value(self):
        total_value = sum(product.price * quantity for product,
                          quantity in self.items)
        return print(f"Total Cart Value: ${total_value:.2f}")

    def show_cart_items(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for product, quantity in self.items:
                print(
                    f"Product Name: {product.name}, Price: ${product.price:.2f}, Quantity: {quantity}")
