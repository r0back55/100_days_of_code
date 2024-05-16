### Section 9 ###


# <----------------------------------------------------------
# Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

# <----------------------------------------------------------
# we retrive values by providing keys:
print(programming_dictionary["Function"])

# we add values by providing key and assign value:
programming_dictionary["Loop"] = "The action of doing something over and over again."

# wipe an existing dictionary:
programming_dictionary = {}

# <----------------------------------------------------------
for key in programming_dictionary.keys():
    print(key)

for value in programming_dictionary.values():
    print(value)

for item in programming_dictionary.items():
    print(item)


# <----------------------------------------------------------
# Excercise
# Instruction: Write a program that converts student scores to grades.

# Grades:
#  scores 91-100: "Outstanding"
#  scores 81-90: "Exeeds Expectations"
#  scores 71-80: "Acceptable"
#  scores 70 or lower: "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 79,
    "Neville": 62,
}

student_grades = {}
for name in student_scores:
    if student_scores[name] > 91:
        student_scores[name] = "Outstanding"
    elif student_scores[name] > 80 and student_scores[name] <=90:
        student_scores[name] = "Exeeds Expectations"
    elif student_scores[name] > 70 and student_scores[name] <=80:
        student_scores[name] = "Acceptable"
    else:
        student_scores[name] = "Fail"
    student_grades[name] = student_scores[name]

print(student_grades)




# <----------------------------------------------------------
# Nesting
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  "total_visits": 15}
}
print(travel_log)

# Nesting dictionaries in a list
travel_log_2 = [
    {
        "Country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
        },
    {
        "Country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  
        "total_visits": 15
        }
]
print(travel_log_2)



# <----------------------------------------------------------
# Nesting Excercise:
# Instruction: Create a function that adds countries you viseted into a travel log

import re

travel_log = [
    {
        "Country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]        
        },
    {
        "Country": "Germany",
        "visits": 15,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
        }
]

def add_new_country(country, visits, cities):
    new_entry = {
        "Country": country,
        "visits": visits,
        "cities": cities
        }
    travel_log.append(new_entry)
    #best_city = new_entry["cities"][0]

    print(f"I have been to {country} {visits} times.")
    print(f"My favourite city was {travel_log[-1]['cities'][0]}.")


country = input("What country you have been to?  \n").title()
visits = input("How many times you visited this country?  \n")
cities = re.split(',|, | ', input("List of cities you visited (comma separated):  \n").title())

add_new_country(country, visits, cities)




# <----------------------------------------------------------
# Secret Auction Program -> VERSION 1 (mine)

import os

more_bidders = True
auction_list = {
    "Winner_Name": 'name',
    "Winner_Bid": 0
}

while more_bidders:
    os.system('cls')
    name = input("What is your name?:  ")
    bid = int(input("What is your bid?:  "))

    if bid > auction_list['Winner_Bid']:
        def auction(name, bid):
            auction_list["Winner_Name"] = name
            auction_list["Winner_Bid"] = bid

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        if should_continue == 'no':
            more_bidders = False

os.system('cls') 
print(f"The winner is {name} with a bid of ${bid}")



# <----------------------------------------------------------
# Secret Auction Program -> VERSION 2 (mine)
import os

more_bidders = True
auction_list = {}

while more_bidders:
    name = input("What is your name?:  ")
    bid = int(input("What is your bid?:  $"))

    def auction(name, bid):
        auction_list[name] = bid
    
    auction(name, bid)

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == 'no':
        more_bidders = False
    os.system('cls')

winner_name = ''
winner_bid = 0
for key,value in auction_list.items():
    if value > winner_bid:
        winner_name = key
        winner_bid = value

os.system('cls') 
print(f"The winner is {winner_name} with a bid of ${winner_bid}")



# <----------------------------------------------------------
# Secret Auction Program -> VERSION 3 (teacher)
import os

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system('cls') 



# <----------------------------------------------------------
# Secret Auction Program -> VERSION 4 (refactored by ChatGPT)
def get_bid():
    """Get a bid from a user."""
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    return name, price

def ask_to_continue():
    """Ask if there are more bidders."""
    return input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

def find_highest_bidder(bidding_record):
    """Find and print the highest bidder from the bidding record."""
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def secret_auction():
    """Conduct a secret auction."""
    bids = {}
    while True:
        name, price = get_bid()
        bids[name] = price
        if ask_to_continue() == "no":
            break
    find_highest_bidder(bids)

# Start the auction
if __name__ == "__main__":
    secret_auction()
