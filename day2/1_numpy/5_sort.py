
import numpy as np

a = [3, 1, 2]
b = np.sort(a)
print("\nOriginal array:", a) 
print("Sorted array:", b) 

# in-place sorting
a = np.array([3, 1, 2])
b = a.sort()
print("\nOriginal array:", a) 
print("Sorted array:", b) 

# structured array sorting
data = np.array([(1, 'Alice', 92), (2, 'Bob', 85), (3, 'Charlie', 87)],
                dtype=[('id', 'i4'), ('name', 'U10'), ('score', 'i4')])

sorted_data = np.sort(data, order='score')
print("\nOriginal array:", data) 
print("Sorted array:", sorted_data)


