import numpy as np

# Original array
original_array = np.array([1, 2, 3, 4, 5])

# Make a copy of the original array
copied_array = original_array.copy()

# Change the original array
original_array[0] = 10

# Display both arrays
print("Original array:", original_array)
print("Copied array:", copied_array)
