### Section 5 ###


# ################################## #
#   Avarage hight of class students  #
# ################################## #
# student_hights = input("Type list of students hights in cm: ").split()
# # converting to a list of integers:
# for n in range(0, len(student_hights)):
#     student_hights[n] = int(student_hights[n])
# sum = 0
# for student in student_hights:
#     print(student)
#     sum += student 
# average = round(sum/len(student_hights),2)
# print(f"Average height for the provided students is: {average}")




# ################################## #
#   Highest score of class students  #
# ################################## #
# student_scores = input("Type list of students scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(f"The highest score was: {max_score}")




# ############################### #
#   adding numbers from 1 to 100  #
# ############################### #
# sum = 0
# for num in range(1, 101):
#     sum += num
# print(f"Sum of 100 numbers is: {sum}")

# sum = 0
# number = 1
# while number <101:
#     sum += number
#     number += 1
# print(f"Sum of 100 numbers is: {sum}")



# #################################### #
#   adding even numbers from 1 to 100  #
# #################################### #
# sum_even = 0
# sum_odd = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         sum_even += number
#     else:
#         sum_odd += number
# print(f"Sum of even numbers is: {sum_even}")
# print(f"Sum of odd numbers is: {sum_odd}")




# #################################### #
#   FizzBuss Game - JOB INVTERVIEW!!!  #
# #################################### #
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 > 0:
#         print("Fizz")
#     elif number % 3 > 0 and number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)




# ##################### #
#   Password Generator  #
# ##################### #
# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
# print("Welcome to the PyPassword Generator!")
# num_letters = int(input("How many letters would you like in your password? "))
# num_numbers = int(input("How many numbers would you like in your password? "))
# num_symbols = int(input("How many symbols would you like in your password? "))

# ### VERSION 1 ###
# random_letters = random.choices(letters, k=num_letters)
# random_numbers = random.choices(numbers, k=num_numbers)
# random_symbols = random.choices(symbols, k=num_symbols)
# combined = random_letters+random_numbers+random_symbols
# print(f"Combined: {combined}")
# random.shuffle(combined)
# print(f"You can use this password: {''.join(combined)}") 

# ### VERSION 2 (easy) ###
# password = ""
# for char in range(1, num_letters+1):
#     password += random.choice(letters)
# for num in range(1, num_numbers+1):
#     password += random.choice(numbers)
# for sym in range(1, num_symbols+1):
#     password += random.choice(symbols)
# print(f"You can use this password: {password}") 

# ### VERSION 3 (hard) ###
# password = ""
# for char in range(1, num_letters+1):
#     password += random.choice(letters)
# for num in range(1, num_numbers+1):
#     password += random.choice(numbers)
# for sym in range(1, num_symbols+1):
#     password += random.choice(symbols)
# final_pass = list(password)
# random.shuffle(final_pass)
# print(f"You can use this password: {''.join(final_pass)}") 