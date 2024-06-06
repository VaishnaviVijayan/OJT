import numpy as np

# Original array
original_array = np.array([1, 2, 3, 4, 5])

# Create a view of the original array
view_array = original_array.view()

# Print the base attribute
print("Original array base:", original_array.base)
print("View array base:", view_array.base)
