import numpy as np

# Define two matrices
matrix1 = np.array([[1, 2, 3],
                     [4, 5, 6]])

matrix2 = np.array([[7, 8],
                     [9, 10],
                     [11, 12]])

# Perform matrix multiplication
result = np.dot(matrix1, matrix2)

print("Result of matrix multiplication using np.dot():")
print(result)
