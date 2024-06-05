import numpy as np

# Create a NumPy array with integer values
int_array = np.array([0, 1, 2, 0, 5])

# Convert the integer array to a boolean array using bool
bool_array = int_array.astype(bool)

# Print the original integer array and the converted boolean array
print("Original integer array:", int_array)
print("Converted boolean array:", bool_array)
print("Data type of the converted array:", bool_array.dtype)
