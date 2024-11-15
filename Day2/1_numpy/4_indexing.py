import numpy as np

# Sample array for demonstrations
array = np.arange(10).reshape(2, 5)  # 2x5 array with values from 0 to 9
print("Original Array:\n", array)

# Basic Indexing 
# Access specific elements by row and column indices
print("\nBasic Indexing")
print("Element at (0, 1):", array[0, 1])  # Element at row 0, column 1 (value 1)
print("Element at (1, 3):", array[1, 3])  # Element at row 1, column 3 (value 8)

# Slice rows and columns
print("First row:", array[0, :])  # All elements in the first row
print("Last column:", array[:, -1])  # All elements in the last column

### 2. Slicing with start, stop, and step ###
print("\nSlicing with start, stop, step")
print("Array[0, 1:5:2]:", array[0, 1:5:2])  # Slice from column 1 to 5 with step 2 on first row

# Negative step (reversing)
print("Reverse last row:", array[1, ::-1])  # Last row, reversed

# Fancy Indexing
# Indexing with integer arrays
print("\nFancy Indexing")
rows = np.array([0, 1])  # Row indices
cols = np.array([1, 3])  # Column indices
print("Elements at (0,1) and (1,3):", array[rows, cols])

# Selecting multiple rows or columns out of order
print("Rows 1 and 0 in reverse order:\n", array[[1, 0], :])  # Reverse order of rows

#Boolean Indexing 
print("\nBoolean Indexing")
# Mask elements greater than 5
mask = array > 5
print("Elements greater than 5:", array[mask])  # Only elements where the condition is True

# Set elements greater than 5 to 0
array[mask] = 0
print("Array after setting elements > 5 to 0:\n", array)

################# Advanved ##############################

# Advanced Indexing
print("\nAdvanced Indexing")
# np.take(): Selects elements at specific indices
take_indices = [0, 2, 4]
print("Using np.take() to select elements [0, 2, 4] in flattened array:", np.take(array, take_indices))

# np.put(): Replaces elements at specific indices
array_copy = array.copy()
np.put(array_copy, [1, 3, 5], [99, 88, 77])  # Replace elements at indices 1, 3, 5 in the flattened array
print("\nArray after np.put():\n", array_copy)

# np.choose(): Select elements from different arrays based on index array
choice_array = np.array([[1, 0, 1], [2, 0, 2]])
choices = np.array([[-10, -20, -30], [10, 20, 30], [100, 200, 300]])
print("\nUsing np.choose() with choices array:\n", np.choose(choice_array, choices))
