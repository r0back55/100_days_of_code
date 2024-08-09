# Read the contents of file1.txt and convert to a list of integers
with open('file1.txt', 'r') as file1:
    numbers1 = [int(line.strip()) for line in file1]

# Read the contents of file2.txt and convert to a list of integers
with open('file2.txt', 'r') as file2:
    numbers2 = [int(line.strip()) for line in file2]

# Find the common numbers between the two lists using list comprehension
result = [num for num in numbers1 if num in numbers2]

print(result)
