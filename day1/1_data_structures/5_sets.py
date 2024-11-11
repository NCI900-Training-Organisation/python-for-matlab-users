'''
Sets in Python are unordered collections of unique elements. They are useful for performing 
mathematical set operations like union, intersection, difference, and more. 
'''

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Add elements

my_set.add(6)
print(my_set)

# update

my_set.update([7, 8, 9])
print(my_set)

# Remove 
my_set.remove(4)
print(my_set)

'''
Remove will raise a error if the element is not available.
'''

# Discard
my_set.discard(4)
print(my_set)

'''
Discard will not raise a error if the element is not available.
'''
# pop
popped_element = my_set.pop()
print("\nPopped element:", popped_element)
print("After popping an element:", my_set)

# Membership
exists = 3 in my_set
print("Does 3 exist in the set?", exists)  

not_exists = 10 in my_set
print("Does 10 exist in the set?", not_exists)

# Length

set_length = len(my_set)
print("\nLength of the set:", set_length)

# Set Operations

my_set = {1, 2, 3, 4, 5}
another_set = {5, 6, 7, 8, 9, 10}

# Union

union_set = my_set | another_set
print("\nUnion:", union_set) 

# Intersection

intersection_set = my_set & another_set
print("Intersection:", intersection_set) 

# Difference: elements in my_set but not in another_set

difference_set = my_set - another_set
print("Difference:", difference_set)

# Symmetric Difference: Elements in either set, but not in both

symmetric_difference_set = my_set ^ another_set
print("Symmetric Difference:", symmetric_difference_set)

# Create from list

list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)

print("\nSet from list (duplicates removed):", unique_set)


