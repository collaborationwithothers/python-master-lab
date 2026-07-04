class Calculator(object):
    """
    A simple calculator class that supports addition and multiplication.
    It also keeps a history of all operations performed.

    >>> calc = Calculator()
    >>> calc.add(2, 3)
    5
    >>> calc.multiply(4, 5)
    20
    >>> len(calc.history)
    2
    """
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"Added {a} to {b} got {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiplied {a} with {b} got {result}")
        return result