import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", np.add(a, b))         
print("Subtraction:", np.subtract(a, b)) 
print("Multiplication:", np.multiply(a, b))  
print("Division:", np.divide(a, b))      


a = np.array([1, 4, 9])

print("\nPower (squared):", np.power(a, 2)) 
print("Exponential:", np.exp(a))          
print("Square root:", np.sqrt(a))         

a = np.array([1, 10, 100])

print("\nNatural Log:", np.log(a))      # Natural logarithm (base e) of each element.
print("Log base 10:", np.log10(a))    # Base-10 logarithm of each element.
print("Log base 2:", np.log2(a))      # Base-2 logarithm of each element.


a = np.array([0, np.pi/2, np.pi])

print("\nSine:", np.sin(a))      
print("Cosine:", np.cos(a))    
print("Tangent:", np.tan(a))   


a = np.array([1.2, 2.5, 3.6, 4.7])

print("\nRounded:", np.round(a))      
print("Floor:", np.floor(a))        
print("Ceil:", np.ceil(a))          
print("Truncated:", np.trunc(a))    



a = np.array([[1, 2, 3], [4, 5, 6]])

print("\nSum:", np.sum(a))             
print("Mean:", np.mean(a))            
print("Median:", np.median(a))        
print("Standard Deviation:", np.std(a)) 
print("Minimum:", np.min(a))         
print("Maximum:", np.max(a))   


a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])

# The smaller array `a` is stretched to match the shape of `b`.
print("\nBroadcasted addition:\n", a + b)  # 






##### Advanced ##################
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("\nDot product:\n", np.dot(a, b))         # Performs matrix multiplication
print("Inverse of a:\n", np.linalg.inv(a))      # Computes the inverse of a matrix a
print("Determinant of a:", np.linalg.det(a))    # 
print("Eigenvalues and Eigenvectors of a:", np.linalg.eig(a))


a = np.array([1, 2, 3, 4, 5])

print("\nWhere greater than 2:", np.where(a > 2, a, 0))   # [0 0 3 4 5]
print("Clipped array:", np.clip(a, 2, 4))               # [2 2 3 4 4]

