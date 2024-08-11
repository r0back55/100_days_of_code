def logging_decorator(func):
    def wrapper(*args):
        # Format the arguments for printing
        formatted_args = ', '.join(map(str, args))
        print(f"You called {func.__name__}({formatted_args})")
        result = func(*args)
        print(f"It returned: {result}")
        return result
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

# a_function(1, 2, 3)


numer = 6 // 3.4
print(type(numer))