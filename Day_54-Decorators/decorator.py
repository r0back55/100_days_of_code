import time


def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        score = end_time - start_time
        print(f"Score for {func.__name__} is: {round(score, 6)} sec.")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
