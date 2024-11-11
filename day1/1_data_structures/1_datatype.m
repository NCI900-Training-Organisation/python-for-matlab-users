
my_int = int32(42);  % Defines a 32-bit integer
disp(my_int);  % Equivalent to Python's print

my_double = 3.14;  % By default, MATLAB treats this as double-precision
disp(class(my_double));  % Display the type of my_double, which should be 'double'

my_string = "Hello, world!";  % Creates a string (not a character array)
disp(my_string);  % Display the string

my_char_array = 'Hello, world!';
disp(my_char_array);