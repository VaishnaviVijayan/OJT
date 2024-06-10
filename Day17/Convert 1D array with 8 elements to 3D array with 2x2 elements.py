import numpy as np

# Create a 1D array with 8 elements
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Reshape the 1D array to a 3D array with dimensions 2x2x2
array_3d = array_1d.reshape((2, 2, 2))

print(array_3d)
