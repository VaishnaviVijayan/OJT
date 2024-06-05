import numpy as np

# Create a NumPy array with float values
float_array = np.array([1.5, 2.8, 3.9, 4.2, 5.7])

# Convert the float array to an integer array using int
int_array = float_array.astype(int)

# Print the original float array and the converted integer array
print("Original float array:", float_array)
print("Converted integer array:", int_array)
print("Data type of the converted array:", int_array.dtype)
