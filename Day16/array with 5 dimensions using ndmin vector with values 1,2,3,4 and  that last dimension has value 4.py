import numpy as np

# Create a vector with values 1, 2, 3, 4
data = [1, 2, 3, 4]

# Create a 5-dimensional array using ndmin
arr = np.array(data, ndmin=5)

# Print the array (optional)
print(arr)

# Get the shape of the array
shape = arr.shape

# Verify the last dimension has value 4
if shape[-1] == 4:
  print("Last dimension has value 4!")
else:
  print("Unexpected shape:", shape)
