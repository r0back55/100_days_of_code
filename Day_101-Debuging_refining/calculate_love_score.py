def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Count occurrences of each letter in the word "TRUE"
    true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')

    # Count occurrences of each letter in the word "LOVE"
    love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')

    # Combine the counts to form a two-digit number
    love_score = int(f"{true_count}{love_count}")

    # Print the love score
    print(love_score)

# Example usage
calculate_love_score("Kanye West", "Kim Kardashian")
