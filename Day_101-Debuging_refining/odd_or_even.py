def odd_or_even(number):
    if not isinstance(number, int):
        return "Input must be an integer."
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

# Example usage
print(odd_or_even(4))  # Output: This is an even number.
print(odd_or_even(7))  # Output: This is an odd number.
print(odd_or_even("a"))  # Output: Input must be an integer.
