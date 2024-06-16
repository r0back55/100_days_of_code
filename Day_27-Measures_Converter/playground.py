def add(*args):
    summ = 0
    for n in args:
        summ += n
    return summ


suma = add(3, 5, 6, 7, 8, 9, 7, 7)


# ---------------------------------------------
def calculator(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


final = calculator(2, add=3, multiply=5)


# ---------------------------------------------
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.sticker = kwargs.get("sticker")


my_car = Car(make="Audi", model="A6")
print(my_car.model)
