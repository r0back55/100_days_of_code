### Section 8 ###


# <----------------------------------------------------------
# Greet Finction

def greet(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet(location="Warsaw", name="Mark")



# <----------------------------------------------------------
# Paint Area Calculator

import math

def paint_calc(heigh, width, cover):
    number_of_cans = math.ceil(heigh*width/cover)
    print(f"You wil need {number_of_cans} cans of paint.")

test_h = int(input("Provide height: "))
test_w = int(input("Provide width: "))
coverage = 5

paint_calc(heigh=test_h, width=test_w, cover=coverage)




# <----------------------------------------------------------
# If the input is prime number

def prime_checker(number):
    counter = 0
    for i in range(2, number):
        if i%2 == 0:
            counter += 1
    if counter > 2:
        print("It is not a Prime Number")
    else:
        print("Yes, it is Prime Number!")

n = int(input(f"Number to check: "))
prime_checker(n)


