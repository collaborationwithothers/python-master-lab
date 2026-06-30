class CoffeeMenuItem(object):
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

menu1 = CoffeeMenuItem(name="Latte", price=5.50, size=20)
menu2 = CoffeeMenuItem(name="Cappuccino", price=4.75, size=16)

print(f"Menu 1: {menu1.name}, Price: ${menu1.price}, Size: {menu1.size}oz")
print(f"Menu 2: {menu2.name}, Price: ${menu2.price}, Size: {menu2.size}oz")

menus = [menu1, menu2]
for menu in menus:
    print(f"Menu Item: {menu.name}, Price: ${menu.price}, Size: {menu.size}oz")

menu_dict = {menu.name: menu for menu in menus}
for name, menu in menu_dict.items():
    print(f"Menu Name: {name}, Price: ${menu.price}, Size: {menu.size}oz")