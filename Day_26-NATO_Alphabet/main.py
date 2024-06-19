import pandas


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type a word:  ").upper()

try:
    fonetic_list = [nato_dict[letter] for letter in user_input]
except KeyError:
    print("Sorry, only letters in the alphabet please")
    user_input = input("Type a word:  ").upper()
else:
    print(fonetic_list)


# Or we can crete a function:
"""
def generate_fonetic_list():
    try:
        fonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_fonetic_list()
    else:
        print(fonetic_list)
"""
