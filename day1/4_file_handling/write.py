
'''
To write data to a file, use "w" or "a" mode. 
"w" mode overwrites the file if it exists, while "a" mode appends to the file.
'''

# Writing to a file
with open("write_file.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Writing to a file in Python.")

# Appending to a file
with open("write_file.txt", "a") as file:
    file.write("\nThis line is appended.")
