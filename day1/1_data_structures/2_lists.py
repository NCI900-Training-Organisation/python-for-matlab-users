

# 1-D list
my_list = [1, 2, 3, 'apple', 'banana', [4, 5, 6]]

# Indexing starts from 0

print(my_list[0]) 
print(my_list[3]) 
print(my_list[5]) 


# 2-D list
two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a 2D list
print(two_d_list[0])
print(two_d_list[0][0])  
print(two_d_list[1][2]) 

# lists can be uneven

two_d_list = [
    [1, 2],
    [4, 5, 6],
    [7, 8, 9, 1, 3]
]

# Modifying a List

# Modifying an element
my_list[1] = 'orange' 
print(my_list)  

# Adding a new element
my_list.append('grapes') 
print(my_list) 

# Inserts an element at a specified index in the list.
print(my_list)
my_list.insert(1, 'apple') 
print(my_list)

# append vs extend

my_list = ['apple', 'banana']
my_list.append([1, 2, 3])
print(my_list)

my_list = ['apple', 'banana']
my_list.extend([1, 2, 3])
print(my_list)

'''
In Python, both `append()` and `extend()` are used to add elements to a list, but they work in 
different ways.

* `append()` adds its argument as a single element to the list.
* `extend()` adds each element of its argument to the list individually.
'''

# Remove elements

'''
* This line uses the remove() method to delete the first occurrence of 'banana' from the list.
* The remove() method only deletes the first instance it finds.
'''

my_list = ['banana', 'banana', 'apple', 'orange', 'green', 'red']
my_list.remove('banana') 
print(my_list) 

'''
* removes and returns the last item in the list, modifying my_list by shortening it by one element.
* If you try to use pop() on an empty list, Python will raise an IndexError since there's nothing 
to remove.
'''
print(my_list)
elt = my_list.pop()
print(elt)
print(my_list)

'''
* The pop() method with an argument removes and returns the element at the specified index. 
Here, 1 is the index, so my_list.pop(1) removes and returns the element at index 1.
'''
print(my_list)
elt = my_list.pop(1)
print(elt)
print(my_list)

'''
This reassigns my_list to a new empty list, which effectively clears its contents.
'''
print(my_list)
my_list.clear()
print(my_list)

'''
List comprehension is a concise and elegant way to create lists in Python. It allows you to generate
a new list by applying an expression to each element in an existing iterable (such as a list, range,
or another collection), optionally including a condition to filter elements.
'''

# Simple List Comprehension

squares = [x ** 2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Using a Condition

evens = [x for x in range(10) if x % 2 == 0]
print(evens)
# Output: [0, 2, 4, 6, 8]

# Applying a Transformation

words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
# Output: ['APPLE', 'BANANA', 'CHERRY']

# Nested List Comprehension

pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(pairs)

