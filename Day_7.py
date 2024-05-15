### Section 7 ###

# #################### #
#   HANGMAN - the Game #
# #################### #

# <---------------------
import random
import Section_7_hangman
import Section_7_word_list

# <---------------------
print(Section_7_hangman.logo)
end_of_game = False

word_list = Section_7_word_list.word_list
stages = Section_7_hangman.stages
chosen_word = random.choice(word_list)
chosen_word_count = len(chosen_word)  #6
lives = 6

display = []
for letter in chosen_word:
    display.append("_")
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("Letter already used, common :)")
        continue

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])