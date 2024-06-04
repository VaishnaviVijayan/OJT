import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Slice from index 3 from the end to index 1 from the end
sliced_array = arr[-(3 + 1): -1]

# Print the sliced array
print(sliced_array)
