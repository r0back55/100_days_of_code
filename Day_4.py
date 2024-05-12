### Section 4 ###
import random


random_integer = random.randint(1,10)
print(random_integer)
random_float = random.random()*5
print(random_float)



# #################### #
#   Coin Toss Program  #
# #################### #
draw1 = random.randint(0, 1)
if draw1 == 0:
    print("Heads")
else:
    print("Tails")

draw2 = random.choice(['Heads', 'Tails'])
print(draw2)




# ##################################### #
#   Select random friends for a dinner  #
# ##################################### #
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
number_of_guests = random.randint(1, len(names))
print(number_of_guests)
guests_list = []
for num in range(1, number_of_guests+1): 
    name = random.choice(names)
    if name not in guests_list:
        guests_list.append(name)
        names.remove(name)
print(guests_list)




# ############### #
#   Treasure Map  #
# ############### #
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure (put like 'B3, C1)? ")
a, b = position
row = str(a).upper()
column = int(b)

if row == 'A':
    line1[column-1] = "X"
elif row == 'B':
    line2[column-1] = "X"
else:
    line3[column-1] = "X"

print(f"{line1}\n{line2}\n{line3}")




# ######################## #
#   Rock, Paper, Scissors  #
# ######################## #
# Rock Paper Scissors ASCII Art

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_objects = [rock, paper, scissors]

print("Hello to 'Rock, Paper, Scissors' game!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

if user_choice > 2 or user_choice <0:
    print("You typed invalid number, you lost!!!")
else:
    print(game_objects[user_choice])
    app_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_objects[app_choice])

    if user_choice == app_choice:
        print("It is a Draw!")
    elif (user_choice == 0 and app_choice == 1) or (user_choice == 1 and app_choice == 2) or (user_choice == 2 and app_choice == 0):
        print("User lost!")
    elif (user_choice == 0 and app_choice == 2) or (user_choice == 1 and app_choice == 0) or (user_choice == 2 and app_choice == 1):
        print("User won!")
    else:
        print("Something went wrong, sorry!")