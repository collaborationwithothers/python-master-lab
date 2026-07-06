class MenuItem(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return f"{self.name}: ${self.price:.2f}"

class CoffeeDrink(MenuItem):
    def __init__(self, name: str, price: float, size: str, coffee_type: str):
        super().__init__(name, price)
        self.size = size
        self.coffee_type = coffee_type

    def get_description(self):
        return f"{self.size} {self.coffee_type} {super().get_description()}"

cofee = CoffeeDrink("Latte", 3.50, "Medium", "Espresso")
print(cofee.get_description())  # Output: Medium Espresso Latte: $3.50