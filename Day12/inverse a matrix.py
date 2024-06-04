import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Compute the inverse of the matrix
inverse_matrix = np.linalg.pinv(matrix)

print("Original matrix:")
print(matrix)
print("\ninverse matrix:")
print(inverse_matrix)
