import numpy as np

# Original array
original_arr = np.arange(10)

# View: Created using slicing
sliced_arr = original_arr[::2]  # Every other element

# Check if sliced_arr is a view
if sliced_arr.base is original_arr:
  print("sliced_arr is a view")
else:
  print("sliced_arr is a copy")
