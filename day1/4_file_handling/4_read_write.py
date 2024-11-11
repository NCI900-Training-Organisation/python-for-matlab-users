

with open("read_write.txt", "r+") as file:
    content = file.read()
    print("Current content:", content)
    file.write("\nAdding new content with r+ mode.")
