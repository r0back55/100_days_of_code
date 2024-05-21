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




# ################# #
#   CESAR CIPHER    #
# ################# #

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# <----------------------------------------------------------
# VERSION 1
def encrypt(plain_text, shift_amount):
    if direction == 'encode':
        original_indexes = []
        for letter in plain_text:
            original_indexes.append(alphabet.index(letter))
        shifted_indexes = []
        for i in original_indexes:
            shifted_indexes.append(i+shift_amount)
        shifted_word = []
        for new_i in shifted_indexes:
            shifted_word.append(alphabet[new_i])
            new_word = ''.join(shifted_word)
        print(f"The encoded text is: {new_word}")
    else:
        original_indexes = []
        for letter in plain_text:
            original_indexes.append(alphabet.index(letter))
        shifted_indexes = []
        for i in original_indexes:
            shifted_indexes.append(i+len(alphabet)-shift_amount)
        shifted_word = []
        for new_i in shifted_indexes:
            shifted_word.append(alphabet[new_i])
            new_word = ''.join(shifted_word)
        print(f"The decoded text is: {new_word}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # <---to avoid indexes out of range for 'alphabet' list

    encrypt(plain_text=text, shift_amount=shift)

    decision = input("Would you like to go again or stop here? Type 'yes' or 'no': \n")
    if decision == 'no':
        should_continue = False