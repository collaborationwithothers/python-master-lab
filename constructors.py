class Greeter(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name}!")
    
    def goodbye(self):
        print(f"Goodbye, {self.name}!")

greeter1 = Greeter("Alice")
greeter1.hello() # Output: Hello, Alice!
greeter1.goodbye() # Output: Goodbye, Alice!

greeter2 = Greeter("Bob")
greeter2.hello() # Output: Hello, Bob!
greeter2.goodbye() # Output: Goodbye, Bob!