import time
import functools
from datetime import datetime, timedelta
import random

def get_exchange_rate(from_currency, to_currency):
    """
    Simulates fetching the exchange rate between two currencies.
    In a real-world scenario, this would involve an API call to a currency exchange service.
    For demonstration purposes, it returns a random exchange rate.
    
    Parameters:
    from_currency (str): The currency code to convert from (e.g., 'USD').
    to_currency (str): The currency code to convert to (e.g., 'EUR').
    
    Returns:
    float: A simulated exchange rate.
    """
    print(f"Fetching exchange rate from {from_currency} to {to_currency}...")
    # Simulate a delay in fetching the exchange rate
    time.sleep(1)
    base_rates = {
        ('USD', 'EUR'): 0.85,
        ('EUR', 'USD'): 1.18,
        ('USD', 'JPY'): 110.0,
        ('JPY', 'USD'): 0.0091,
        ('EUR', 'JPY'): 129.53,
        ('JPY', 'EUR'): 0.0077}
    rate = base_rates.get((from_currency, to_currency), 1.0)  # Default to 1.0 if the pair is not found
    # Return a random exchange rate for demonstration purposes
    return round(rate + random.uniform(0.5, 1.5), 4)

def cache_wth_ttl(ttl_seconds):
    """
    A decorator that caches the result of a function for a specified time-to-live (TTL) duration.
    
    Parameters:
    ttl_seconds (int): The time-to-live duration in seconds for the cached result.
    
    Returns:
    function: The decorated function with caching behavior.
    """
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create a unique key based on the function arguments
            key = (args, frozenset(kwargs.items()))
            current_time = datetime.now()
            # Check if the result is in the cache and still valid
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < timedelta(seconds=ttl_seconds):
                    print(f"Returning cached result for {func.__name__} with args {args} and kwargs {kwargs}")
                    return result
                else:
                    print(f"Cache expired for {func.__name__} with args {args} and kwargs {kwargs}")
            # Call the original function and cache the result
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator

@cache_wth_ttl(ttl_seconds=5)
def get_exchange_rate_cached(from_currency, to_currency):
    """
    Fetches the exchange rate between two currencies with caching.
    
    Parameters:
    from_currency (str): The currency code to convert from (e.g., 'USD').
    to_currency (str): The currency code to convert to (e.g., 'EUR').
    
    Returns:
    float: The exchange rate between the two currencies.
    """
    return get_exchange_rate(from_currency, to_currency)

print(get_exchange_rate_cached("USD", "EUR"))  # Fetches and caches the result
time.sleep(2)
print(get_exchange_rate_cached("USD", "EUR"))  # Returns cached result
time.sleep(4)
print(get_exchange_rate_cached("USD", "EUR"))  # Cache expired, fetches again