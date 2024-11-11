import numpy as np

arr = np.random.rand(3, 4)
print("Array : ")
print(arr)


arr = arr.reshape((6, 2))
print("\nReshaped : ")
print(arr)

'''
reshape does not always create a copy in NumPy.

If the array can be reshaped without changing the underlying data layout (i.e., the elements are 
still stored in contiguous memory for the new shape), reshape will return a view of the original 
array. This means that modifying the reshaped array will also affect the original array.

If the requested shape is incompatible with the data's memory layout (e.g., the elements are not 
contiguous in the desired order), reshape will create a copy of the data with the new shape.

'''

reshaped_copy = arr.reshape(2, 6).copy() # force a copy
print("\nReshaped copy: ")
print(reshaped_copy)

# creates a new, independent 1-D array with the data in a single dimension. Modifications to the 
# flattened array won't affect the original.
arr1 = arr.flatten()
print("\nFlatten : ")
print(arr1)

arr = np.random.rand(1, 4)
print("\n Transpose : ")
print(arr.T)

print("\n Transpose : ")
print(arr.transpose())

'''
resize modifies the original array in-place.

If the new shape has more elements than the original array, the array is resized, and the new 
elements are filled with zeros. If it has fewer elements, the array is truncated to fit the new 
shape.

Resizw doesn't require that the number of elements stay the same. The resize method alters the 
original array, potentially adding or removing elements.
'''

arr = np.arange(6)
arr.resize(3, 3)  # Resize to 3x3, filling with zeros
print("\n Resize : ")
print(arr)


############## Additional information  ############## 

# expand
# Original 1D array
arr = np.array([1, 2, 3])
print("\n Original array:")
print(arr)


# Expand dimensions by adding a new axis at the beginning (axis=0)
expanded_arr = np.expand_dims(arr, axis=0)
print("\n Expanded array (axis=0):")
print(expanded_arr)

# Expand dimensions by adding a new axis at the end (axis=-1)
expanded_arr_end = np.expand_dims(arr, axis=-1)
print("\n Expanded array (axis=-1):")
print(expanded_arr_end)


# squueze
# Create an array with singleton dimensions
arr = np.array([[[1, 2, 3]]])  # Shape (1, 1, 3)

print("\n Original array (squeeze):")
print(arr)
print("shape", arr.shape)

# Squeeze the array to remove all singleton dimensions
squeezed_arr = np.squeeze(arr)

print("\nSqueezed array:")
print(squeezed_arr)
print("Shape of squeezed array:", squeezed_arr.shape)

