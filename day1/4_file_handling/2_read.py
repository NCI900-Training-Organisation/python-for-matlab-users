
'''
using a with statement automatically handles closing the file.
'''


# read(): Reads the entire content of the file as a string.
print("----- read() operations ------")
with open("sample.txt", "r") as file:
    # File operations
    content = file.read()
    print(content)

# readline(): Reads a single line from the file
print("----- readline() operations ------")
with open("sample.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())  # Removes newline characters
        line = file.readline()

# readline(): Reads a single line from the file
print("----- readlines() operations ------")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)