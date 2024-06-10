import numpy as np

# Create a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Method 1: Using reshape
array_1d_reshape = array_3d.reshape(-1)


print("Using reshape:", array_1d_reshape)

