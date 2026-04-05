import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

# Maximum value in the array
my_array.max()  # Output: 5

# Minimum value in the array
my_array.min()  # Output: 1

# Sum of all elements in the array
my_array.sum()  # Output: 15

# Array Methods
np.zeros(5)  # Output: array([0., 0., 0., 0., 0.])
np.ones(5)   # Output: array([1., 1., 1., 1., 1.])

# Random numbers
np.random.random(5) # Output: array of 5 random numbers between 0 and 1, e.g., array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])
np.random.rand(5)  # Output: array of 5 random numbers between 0 and 1, e.g., array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])
np.random.rand(3,3) # Output: 3x3 array of random numbers between 0 and 1, e.g., array([[0.5488135 , 0.71518937, 0.60276338], [0.54488318, 0.4236548 , 0.64589411], [0.43758721, 0.891773 , 0.96366276]])
np.random.randint(0, 10, 5) # Output: array of 5 random integers between 0 and 9, e.g., array([3, 7, 2, 5, 1])

# The type of my_array is a NumPy array
type(my_array)  # Output: <class 'numpy.ndarray'>

# Arange function to create an array of evenly spaced values
np_array = np.arange(0,10) # Output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np_array = np.arange(0, 10, 2)  # Output: array([0, 2, 4, 6, 8])

# Indexing
np_array[0] # Output: 0
np_array[-1] # Output: 8

# Slicing [start:stop:step]
np_array[1:4] # Output: array([2, 4, 6])
np_array[1:] # Output: array([2, 4, 6, 8])
np_array[:3] # Output: array([0, 2, 4])
np_array[::2] # Output: array([0, 4, 8])
np_array[1:2:3] # Output: array([2])

# Arithmetic Operations
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [10, 20, 30, 40, 50]

my_array1 = np.array(my_list1)
my_array2 = np.array(my_list2)

# AO: Addition
my_array1 + my_array2  # Output: array([11, 22, 33, 44, 55])

# AO: Subtraction
my_array2 - my_array1  # Output: array([9, 18, 27, 36, 45])

# AO: Multiplication
my_array1 * my_array2  # Output: array([ 10,  40,  90, 160, 250])
my_array1 * 2  # Output: array([ 2,  4,  6,  8, 10])

# AO: Division
my_array2 / my_array1  # Output: array([10., 10., 10., 10., 10.])

# Matrix
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix3 = np.array([5, 6])
matrix4 = np.array([[7], [8]])

# Matrix: Accessing elements in a matrix with indexing
matrix1[0][1] # Output: 2

# Matrix: Shape of the matrix
matrix1.shape # Output: (2, 2)

# Matrix: Sum of all elements in the matrix
matrix1.sum() # Output: 10

# Matrix: Element-wise addition of two matrices
matrix1 + matrix2 # Output: array([[6, 8], [10, 12]])
matrix1 + matrix3 # Output: array([[6, 8], [8, 10]])
matrix1 + matrix4 # Output: array([[8, 9], [10, 11]])

# Matrix: Dot product of two matrices
matrix5 = np.array([[1, 2, 3], [4, 5, 6]])
matrix6 = np.array([[7, 8], [9, 10], [11, 12]])

np.dot(matrix5, matrix6) # Output: array([[58,  64], [139, 154]])

# Matrix: Random matrix
np.random.random((2, 3)) # Output: 2x3 array of random numbers between 0 and 1, e.g., array([[0.5488135 , 0.71518937, 0.60276338], [0.54488318, 0.4236548 , 0.64589411]])

# Matrix: Reshaping a matrix
matrix5.reshape(3, 2) # Output: array([[1, 2], [3, 4], [5, 6]])

# Matrix: Transpose of a matrix
matrix6.T # Output: array([[7, 9, 11], [8, 10, 12]])

# Matrix: Operations on matrices
array1 = np.random.randint(1, 100, 5) # Output: array of 5 random integers between 1 and 99, e.g., array([83, 53, 70, 44, 60])

# Matrix: Operations -> Conditional selection
array1 > 50 # Output: array([ True,  True,  True, False,  True])
array1[array1 > 50] # Output: array of elements in array1 that are greater than 50, e.g., array([83, 53, 70, 60])

# Matrix: Operations -> z-score normalization
matrix7 = np.array([1, 2, 3, 4, 5])
mean = matrix7.mean() # Mean of the matrix, Output: 3.0  
std = matrix7.std() # Standard deviation of the matrix, Output: 1.4142135623730951
z_score = (matrix7 - mean) / std # Z-score normalization, Output: array([-1.41421356, -0.70710678,  0.        ,  0.70710678,  1.41421356])

# Matrix: Operations -> Math Equations
# Example: Solving a system of linear equations
# 2x + 3y = 5
# 4x + 5y = 6
A = np.array([[2, 3], [4, 5]]) # Coefficient matrix
B = np.array([5, 6]) # Constant matrix

solution = np.linalg.solve(A, B) # Output: array([-1., 3.])

# Matrix: Operations -> Linspace
# Linspace is used to create an array of evenly spaced values between a specified start and end point.
np_linspace = np.linspace(0, 10, 5) # Output: array([ 0., 2.5, 5., 7.5, 10.])