import numpy as np

array = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 4, 4])

# Get unique values and their counts
unique_values, counts = np.unique(array, return_counts=True)

# Create a dictionary to store unique values and their counts
frequency_dict = dict(zip(unique_values, counts))

# Print the frequency of unique values
print("Frequency of unique values:")
for value, count in frequency_dict.items():
    print(f"{value}: {count}")
