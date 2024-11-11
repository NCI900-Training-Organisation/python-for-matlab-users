'''
Dictionaries in Python are mutable, unordered collections of key-value pairs. They are widely 
used for storing and retrieving data based on keys. Here’s how to create a dictionary and perform 
various operations on it.
'''

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "travelling", "swimming"]
}
print(my_dict)

# Indexing

print(my_dict["name"]) 
print(my_dict["hobbies"])
print(my_dict["age"])

# Adding or Updating Key-Value Pairs

my_dict["occupation"] = "Engineer"
print("After adding occupation:", my_dict)

my_dict["age"] = 31
print("After updating age:", my_dict)  

# Removing Key-Value Pairs

# Using del
del my_dict["city"]
print("After deleting city:", my_dict)

# Using pop
age = my_dict.pop("age")
print("After popping age:", my_dict)  
print("Popped age:", age)  

# Membership

exists = "name" in my_dict
print("Is 'name' a key in the dictionary?", exists)  

not_exists = "city" in my_dict
print("Is 'city' a key in the dictionary?", not_exists)  

# Getting All Keys and Values

keys = my_dict.keys()
print("Keys:", list(keys))  

values = my_dict.values()
print("Values:", list(values))

items = my_dict.items()
print(items) 

items = list(items)
print(items)

# Merging

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "travelling", "swimming"]
}

another_dict = {
    "email": "alice@example.com",
    "age": 31  # This will update the age in my_dict_copy
}

# Using update
my_dict.update(another_dict)

print(my_dict)


# or

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "travelling", "swimming"]
}

another_dict = {
    "email": "alice@example.com",
    "age": 31  # This will update the age in my_dict_copy
}

# Using update
merged_dict = my_dict | another_dict

print(my_dict)
