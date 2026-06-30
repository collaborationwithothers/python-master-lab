class ShoppingCart(object):
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
    
    def add_item(self, item):
        self.items.append(item)
        return self.items
    
    def share_cart(self, other_cart):
        other_cart.items = self.items.copy()
        return other_cart

cart1 = ShoppingCart()
cart2 = ShoppingCart()
cart2 = cart1
cart1.add_item("Apple")
print(f"Cart 1 items: {cart1.items}")
print(f"Cart 2 items: {cart2.items}")