# Reading a binary file
with open("python.jpeg", "rb") as file:
    binary_data = file.read()

# Writing to a binary file
with open("python_new.jpeg", "wb") as file:
    file.write(binary_data)

'''

1. Encoding and Decoding
-------------------------

* Text Files: In text mode ("r" or "w"), Python reads and writes data as text (strings). 
Text mode automatically handles encoding and decoding (e.g., UTF-8), translating between 
human-readable text and the byte representation stored on disk. This process interprets newline 
characters based on the platform (e.g., \n on Linux, \r\n on Windows).
* Binary Files: In binary mode ("rb" or "wb"), data is read or written as raw bytes. Python doesn’t 
apply any encoding or decoding, and data is read exactly as it appears in the file. 
This is important for files where every byte counts, such as images, videos, or executable files.

2. Platform-Specific Newline Handling
--------------------------------------
* In text mode, Python automatically handles newline characters. For example, it will translate 
\n to \r\n when writing a file on Windows to match the platform’s newline convention.

* In binary mode, newline characters are read and written as-is without any translation. 
This ensures that binary data is consistent across different platforms.

3. Preventing Corruption of Non-Text Files
--------------------------------------------
* Binary files (like images, videos, and executables) contain data in non-text formats, often 
represented as arbitrary byte sequences. Reading or writing these files in text mode could 
corrupt their contents if Python attempts to interpret or modify those byte sequences as text.

* Binary mode preserves the integrity of the file by treating each byte as raw data without any 
interpretation or conversion, which is essential for accurately working with non-text files.

'''