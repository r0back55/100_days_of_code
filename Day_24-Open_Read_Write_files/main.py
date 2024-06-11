# Define the placeholder text that will be replaced with names in the letter
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    # Read all names from the file into a list
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    # Read the entire contents of the letter template
    letter_contents = letter_file.read()

    for name in names:
        # Remove any leading/trailing whitespace from the name
        name_stripped = name.strip()

        # Replace the placeholder in the letter template with the current name
        new_letter = letter_contents.replace(PLACEHOLDER, name_stripped)

        # Open a new file for writing the personalized letter
        with open(f"./Output/ReadyToSend/letter_for_{name_stripped}.txt", mode="w") as final_letter:
            # Write the personalized letter to the new file
            final_letter.write(new_letter)
