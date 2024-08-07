def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example usage
print(is_leap_year(2400))  # Output: True
print(is_leap_year(1989))  # Output: False
