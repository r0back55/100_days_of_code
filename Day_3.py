### Section 3 ###


# ############## #
#   Odd or Even  #
# ############## #
number = int(input("Please provide a number: "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")




# ########## #
#   Tickets  #
# ########## #
# hieght = int(input("What is your hieght in cm? "))
if hieght > 120:
    print("You are free to go!")
    age = int(input("What is your age: "))
    if age > 18:
        print("You have to pay $12")
    elif age <12:
        print("You have to pay $5")
    else:
        print("You have to pay $7")
else:
    print("You have to grow taller to use rollercaster")




# ##################### #
#   BMI calculator 2.0  #
# ##################### #
weight = float(input("Input your weight in kg: "))
hight = float(input("Provide your hieught in meters: "))
bmi = round(weight/hight**2,5)

if bmi < 18.5:
    print(f"Your BIM is {bmi}, you are underweightes.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BIM is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BIM is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BIM is {bmi}, you are obese.")
else:
    print(f"Your BIM is {bmi}, you are clinially obese.")




# ######################### #
#   LEAP YEAR calculator    #
# ######################### #
year = int(input("Please provde a year: "))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Leap year")
    elif year % 100 > 0 and year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")




# ############## #
#   Tickets 2.0  #
# ############## #
hieght = int(input("What is your hieght in cm? "))
bill = 0
if hieght > 120:
    print("You are free to go!")
    age = int(input("What is your age: "))
    if age > 18:
        if age >45 and age < 55:
            print("Great, you receive free ticket!")
        else:
            bill = 12
            print("Adult tickets are $12")
    elif age <12:
        bill = 5
        print("Child tickets are $5")
    else:
        bill = 7
        print("Youth tickets are $7")
    answer = input("Do you want a photo taken? Y or N ")
    if answer == 'Y':
        bill += 3
    print(f"Please pay: ${bill}")
else:
    print("You have to grow taller to use rollercaster")




# ######################## #
#   Pizza Order Program    #
# ######################## #
size = input("What size of pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
if size == 'S':
    price = 15
    if add_pepperoni == 'Y':
        price += 2
    if extra_cheese == 'Y':
        price += 1
elif size == 'M':
    price = 20
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
else:
    price = 25
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
print("Thank you for choosing Python Pizza Deliveris!")
print(f"Your final bill is: ${price}")




# ########################## #
#   Love score calculator    #
# ########################## #
name1 = input("What is your name? ").upper()
name2 = input("What is her name? ").upper()
name_combined = name1+name2

true = 0
love = 0
for letter in name_combined:
    if letter in "TRUE":
        true += 1
    if letter in "LOVE":
        love += 1

love_score = str(true)+str(love)
print(f"Your score is: {love_score}")




# ######################### #
#   Treasury island game    #
# ######################### #
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to  Treasury Island")
print("Your mission is to find the treasure")
first = input("You are at a corss road. Where do you want to go? Type 'left' or 'right': ")

if first == 'left':
    swim_wait = input("Do you want to swim or wait for a boat? Type 'swim' or 'wait': ")
    if swim_wait == 'wait':
        door = input("Which door do you want to open? Type 'red' or 'yellow' or 'blue': ")
        if door == 'yellow':
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")