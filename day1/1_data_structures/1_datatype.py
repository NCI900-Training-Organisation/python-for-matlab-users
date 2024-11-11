


'''
Integer
--------

Unlike many other languages, Python doesn’t have a maximum value for integers. When the value of an 
integer grows beyond the typical 32- or 64-bit limit, Python automatically allocates more space for 
the integer, preventing overflow.
'''

my_int = 42 # my_int = int32(42)
print(my_int)

'''

Float
------

Python does not distinguish between float and double as other languages like C++ do. Instead, 
all floating-point numbers are treated as float (double-precision) by default, so Python’s 
float already offers what is considered double precision.
'''

my_double = 3.14 # my_double = 3.14;
print(type(my_double))

'''
Strings
--------
'''

my_string = "Hello, world!" # my_string = 'Hello, world!';
print(my_string)