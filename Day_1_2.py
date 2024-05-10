### Section 1,2 ###


# ##################### #
#   Greeting generator  #
# ##################### #
citi = input("What is the name of the citi you grew up in?\n")
pet_name = input("What is your pet's name?\n")

print(f"Your brand name could be {citi} {pet_name}")





# ##################################### #
#   Sum of digits in a provided number  #
# ##################################### #
number = input("Please provide a number to calculate: ")
length = len(number)
sum = 0

for num in number:
    sum += int(num)

print(f"Sum of digits is equal to: {sum}")




# ################# #
#   BMI calculator  #
# ################# #
weight = float(input("Input your weight in kg: "))
hight = float(input("Provide your hieught in meters: "))
bmi = round(weight/hight**2,2)

print(f"Your BMI is: {bmi}")




# ############################# #
#   'Life in weeks' calculator  #
# ############################# #
age = input("What is your age? ")
max_age = 90
time_left = (max_age-int(age))*56

print(f"You have {time_left} weeks left")




# ################# #
#   Tip calculator  #
# ################# #
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip_percent = float(input("How much tip would you like to give (10%, 12%, or 15%)? "))
people = float(input("How many people to split the bill? "))
pay_per_person = round(bill*(1+tip_percent/100)/people, 2)

print(f"Each person should pay ${pay_per_person}")
