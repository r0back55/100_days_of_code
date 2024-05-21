### Section 14 ###
### VSCode  ###


# <----------------------------------------
###########  Higher Lower Game  ###########

# <------------- 1st Version --------------
from Day_14_art import logo, vs
from Day_14_data import data
import random
import os

score = 0
continue_game = True

# <----------------------------------------
# Draw a random comaprison
option_a = random.randint(0, len(data)-1)
del data[option_a]  # <-- to avoid situation where a == b
option_b = random.randint(0, len(data)-1)


while continue_game == True:
    # <----------------------------------------
    # Display art
    print(logo)


    # <----------------------------------------
    # Display current score
    print(f"Current score is: {score}")    
    print(f"Compare A: {data[option_a]['name']}, {data[option_a]['description']} from {data[option_a]['country']}")
    print(vs)
    print(f"Against B: {data[option_b]['name']}, {data[option_b]['description']} from {data[option_b]['country']}")


    # <----------------------------------------
    # Ask a user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B':  ").upper()
    

    # <----------------------------------------
    ## Get the followers count:
    option_a_followers = data[option_a]['follower_count']
    option_b_followers = data[option_b]['follower_count']

    ## Check if user is correct:
    if user_guess == 'A' and option_a_followers > option_b_followers:
        print("You are right!")
        score += 1
        option_b = random.randint(0, len(data)-1)
        os.system('cls') 
    elif user_guess == 'B' and option_a_followers < option_b_followers:
        print("You are right!")
        score += 1
        option_a = option_b
        option_b = random.randint(0, len(data)-1)
        os.system('cls') 
    else:
        print(f"Sorry, that's wrong. Your score is: {score}")
        continue_game = False
    
# <------------- 1st Version --------------

# TODO 1: something to do