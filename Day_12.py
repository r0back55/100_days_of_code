### Section 12 ###


# # <-----------------------------------------
# # Scopes #
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside the function: {enemies}")



# # <-----------------------------------------
# # Global Scopes #
# player_health = 10  # << global variable

# def game():
#     def drink_potion():     # << local function
#         potion_strength = 2     # << local variable
#         print(player_health)
#     drink_potion()

# print(player_health)

# # if you create a variable "within a function" - it is by defauls availavle only "within that function"
# # 'if' / 'while' / 'for' blocks they dont count as creation of local scopes



# # <-----------------------------------------
# # Modify Global Scopes #
# enemies = 1

# def increase_enemies():
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"Enemies outside the function: {enemies}")



# # <-----------------------------------------
# # Global Constatns #
# # variables that you define and never plan to change them later on

# # to differenciate it from normal variables it has been 'agreed' to use UPPERCASE
# MY_HIGHT = 172
# PI = 3.14159




# <-----------------------------------------
# Number Guessing Game #
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def guessing_game():
    # setting up difficulty level that will determine number of attempts:
    difficulty = input("Choose difficulty. Type 'easy' or 'hard':  ") 
    if difficulty == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts.")
    else:
        attempts = 5
        print(f"You have {attempts} attempts.")
    
    # choosing a random number between 1 and 100:
    answer = random.randint(1,100)

    # allowing user to choose a number between 1 and 100:
    guess = int(input("Make a guess:  "))

    # while loop to count the attempts:
    while attempts > 1:
        if guess == answer:
            print("You win!")
            print(f"Correct number is: {answer}")
            break
        elif guess > answer:
            print("Too high.")
            guess = int(input("Make a guess:  "))
        else:
            print("Too low.")
            guess = int(input("Make a guess:  "))
        attempts -= 1
    else:
        print("You run out of moves! You loose!")

    # allowing user to play again or terminate the game:
    play_again = input("Do you want to play again? Type 'y' or 'n':  ")
    if play_again == 'y':
        guessing_game()
    else:
        print("Thank you for playing!")


# running the actual game by calling the function:
guessing_game()

