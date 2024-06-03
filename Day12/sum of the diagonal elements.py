import numpy as np
# 3*3 Array
array_3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# Calculate the sum of diagonal elements
diagonal_sum_3x3 = np.trace(array_3x3)

print(f"The sum of diagonal elements of the 3x3 array is: {diagonal_sum_3x3}")


# 4*4 array
array_4x4 = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])

# Calculate the sum of diagonal elements
diagonal_sum_4x4 = np.trace(array_4x4)

print(f"The sum of diagonal elements of the 4x4 array is: {diagonal_sum_4x4}")

