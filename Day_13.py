### Section 13 ###
### VSCode  ###


#<----------------------------------------
##############  Debugging  ###############

#uncomment to test the code blocks and find issues


# Describe Problem
def my_function():
  for i in range(1, 20):  # <-- for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()
# the bug here is because range takes number from 1 to 20 exclusive, so it takes from 1 to 19



# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)   # <-- randint(0, 5)
print(dice_imgs[dice_num])
# the bug here is that randint draw numbers from 1 to 6, 
# and list has indexes from 0 to 5, so once the number 6
# is drawn, the list item is out of range



# Play Computer
year = int(input("What's your year of birth?  "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:   # <-- elif year >= 1994:
  print("You are a Gen Z.")
# bug1 - is tht 1994 is excluded
# bug2 - here is with missing else statement, when someone was born before 1980



# Fix the Errors
age = input("How old are you?")
if age > 18:
print(f"You can drive at age {age}.")
# bug1 - print is not indented
# bug2 - print stetement is missing "f"
# bug3 - missing int() for input



#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
# bug1 - comparison "==" instead of assignment "="



#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)
mutate([1,2,3,5,8,13])
# bug1 - "b_list.append(new_item)"" should be indented



#Even/Odd number
number = int(input()) # which number do you want to check?
if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
# bug1 - user don't know what to do after running program
# bug2 - "if number % 2 = 0:" << assignment "=" cinstead of omparison "=="
