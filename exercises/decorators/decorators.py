import time
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        A decorator that measures the execution time of a function."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def process_payment(amount, payment_method="credit_card"):
    print(f"Processing payment of ${amount} using {payment_method}...")
    time.sleep(2)  # Simulate a delay in processing
    print("Payment processed successfully!")


print("Starting payment processing...")
process_payment(100, "credit_card")
print(f"function name: {process_payment.__name__}")
print(f"function docstring: {process_payment.__doc__}")