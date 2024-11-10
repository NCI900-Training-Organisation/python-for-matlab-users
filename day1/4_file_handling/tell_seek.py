with open("sample.txt", "r") as file:
    print(file.tell())  # Current position: 0
    file.read(5)
    print(file.tell())  # Position after reading 5 characters
    file.seek(0)  # Move back to the beginning
    print(file.read(5))  # Read the first 5 characters again
