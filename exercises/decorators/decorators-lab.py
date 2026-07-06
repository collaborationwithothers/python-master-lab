import functools
from datetime import datetime, timedelta
import time
def timed(func):
    """
    A decorator that measures the execution time of a function.
    
    Parameters:
    func (function): The function to be decorated.
    
    Returns:
    function: The decorated function with timing behavior.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper



def sayhello(name):
    """
    A simple function that greets the user by name.
    
    Parameters:
    name (str): The name of the user to greet.
    
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

sayhello = timed(sayhello)
sayhello("Alice")  # Output: Hello, Alice!
print(sayhello.__name__)  # Output: sayhello
print(sayhello.__doc__)   # Output: A simple function that greets the user