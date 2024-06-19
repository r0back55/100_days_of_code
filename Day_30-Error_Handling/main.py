# FileNotFoundError
"""
try:
    file = open("./a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])

except FileNotFoundError:
    file = open("./a_file.txt", mode="w")
    file.write("Something")

except KeyError as error_message:
    print(f"That key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File has been closed")
"""


# Raising our own exceptions:
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 2:
    raise ValueError("This is not realistic human height!")

bmi = weight / height**2
print(bmi)
