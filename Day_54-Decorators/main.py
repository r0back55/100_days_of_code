import time


# Python decorator function:
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


@delay_decorator # this is how we use decorators
def say_hello():
    print("Hello")


def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")
