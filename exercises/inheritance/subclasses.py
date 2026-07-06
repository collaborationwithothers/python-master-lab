class Pet(object):
    sound = ""
    def __init__(self, name):
        self.name = name

    def speak(self):
        kind_of_pet = self.__class__.__name__
        return f"{kind_of_pet} says {self.sound}!"

class Dog(Pet):
    sound = "Woof"

class Cat(Pet):
    sound = "Meow"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Dog says Woof!
print(cat.speak())  # Output: Cat says Meow!