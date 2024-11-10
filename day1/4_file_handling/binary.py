# Reading a binary file
with open("python.jpeg", "rb") as file:
    binary_data = file.read()

# Writing to a binary file
with open("python_new.jpeg", "wb") as file:
    file.write(binary_data)
