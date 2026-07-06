import functools

def validate_types(*expected_arg_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_arg_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} of {func.__name__} must be of type {expected_type.__name__}, got {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, str)
def process_payment(amount, payment_method):
    """
    Processes a payment with the given amount and payment method.
    
    Parameters:
    amount (int): The amount to be processed.
    payment_method (str): The method of payment (e.g., 'credit_card', 'paypal').
    
    Returns:
    None
    """
    print(f"Processing payment of ${amount} using {payment_method}...")

print(process_payment(100, "credit_card"))  # Valid call
print(process_payment("100", "credit_card"))  # Invalid call, will raise TypeError