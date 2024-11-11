
import numpy as np

# From list
arr = np.array([1, 2, 3])
print("from list : ")
print(arr)

# From tuple
arr = np.array((1, 2, 3, 4, 5))
print("\n from tuple : ")
print(arr)

# Initialise
arr = np.zeros((2, 3))
print("\n Initialise zeros : ")
print(arr)

arr = np.ones((2, 3))
print("\n Initialise ones : ")
print(arr)

arr = np.empty((2, 3))
print("\n Empty array : ")
print(arr)

arr = np.identity(3)
print("\n Identity matrix : ")
print(arr)

start = 0
stop = 10
step = 3
arr = np.arange(start, stop, step)
print("\n Arrange : ")
print(arr)


# Generate 5 values evenly spaced between 0 and 10, inclusive
arr = np.linspace(0, 10, num=5)
print("\n Numspace : ")
print(arr)

# Random numbers

arr = np.random.rand(3, 2) # values between 0 and 1
print("\n Random : ")
print(arr)

arr = np.random.randint(1, 10, size=(3, 2)) # values between 2 numbers
print("\n Random : ")
print(arr)

# Generate random floats between 1 and 10
arr = 1 + 9 * np.random.rand(3, 2)
print("\n Random : ")
print(arr)