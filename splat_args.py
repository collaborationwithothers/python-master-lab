def smallest_and_largest(*args):
    if not args:
        return None, None
    smallest = min(args)
    largest = max(args)
    return smallest, largest

print(smallest_and_largest(3, 1, 4, 1, 5, 9))  # Output: (1, 9)

def apply_functions(value, **kwargs):
    return {key: func(value) for key, func in kwargs.items()}

print(apply_functions('AbCd', upper=str.upper, lower=str.lower, len=len))  # Output: {'upper': 'ABCD', 'lower': 'abcd', 'len': 4}