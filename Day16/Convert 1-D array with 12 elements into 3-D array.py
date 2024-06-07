import numpy as np

# Sample 1D array
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Reshape into a 3D array with 2 outer arrays, each containing 3 sub-arrays of 2 elements
reshaped_array = np.reshape(data, (2, 3, 2))

# Print the 3D array (optional)
print(reshaped_array)
