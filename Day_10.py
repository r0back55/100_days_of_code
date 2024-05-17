### Section 10 ###


# <----------------------------------------------------------
# Functions with outputs

def format_name(f_name, l_name):
    f_name.title()
    l_name.title()
    return f"{f_name.title()} {l_name.title()}"

changed = format_name("robert", "chwedczuk")
print(changed)




# <----------------------------------------------------------
# program that will tell how many days are in any in a given month

def is_leap_year(year):
  if year % 4 == 0:
      if year % 100 == 0 and year % 400 == 0:
          return True
      elif year % 100 > 0 and year % 4 == 0:
          return True
      else:
          return False
  else:
      return False

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month-1]

year = int(input("Please provide a year: "))
month = int(input("Please provide a month (as number): "))

print(f"Is leap year? {is_leap_year(year)}")
print(f"Days in given month: {days_in_month(year, month)}")




# <----------------------------------------------------------
# Docstrings - description of function within ''' '''

def format_name(f_name, l_name):
    '''Takes the first and last name and format it
    to return the title case veriosn of the name.'''

    f_name.title()
    l_name.title()
    return f"{f_name.title()} {l_name.title()}"

changed = format_name("robert", "chwedczuk")
print(changed)




# <----------------------------------------------------------
# Building CALCULATOR

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
  num1 = float(input("What is the first number?  "))
  for symbol in operations:
    print(symbol)
  continue_program = True

  while continue_program:
    symbol = input("Pick an operation:  ")
    num2 = float(input("What is the next number?  "))
    calculation_function = operations[symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue with {answer} \n Type 'n' to start new calculation or \n Type 'x' to exit:  ") == 'y':
      num1 = answer
    else:
      continue_program = False
      print("Thank you for using my calculator!")
      calculator()

calculator()