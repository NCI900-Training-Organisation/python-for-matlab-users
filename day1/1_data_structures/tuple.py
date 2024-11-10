
'''
Tuples in Python are immutable sequences that can hold a collection of items. They are similar to 
lists but have a few key differences, such as being immutable (you cannot change their content 
after creation).
'''
my_tuple = (1, 'red', 3, "green", 5)
print("Original tuple:", my_tuple)

# Indexing

print(my_tuple[1])
print(my_tuple[4])
print(my_tuple[5])

index_of_3 = my_tuple.index(3)
print("Index of 3 in the tuple:", index_of_3)

# Slicing
sliced_tuple = my_tuple[1:4]
print(sliced_tuple)

# Concatenate
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Repetition
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# Membership
exists = 3 in my_tuple
print("Does 3 exist in the tuple?", exists) 

not_exists = 10 in my_tuple
print("Does 10 exist in the tuple?", not_exists) 

# Length
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)

# Counting
count_of_2 = my_tuple.count(2)
print("Count of 2 in the tuple:", count_of_2)


# Nested tuple
nested_tuple = (my_tuple, another_tuple)
print("Nested tuple:", nested_tuple)

print(nested_tuple[0])
print(nested_tuple[1])