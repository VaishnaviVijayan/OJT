#Data Type of a NumPy Array Object:
import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
array_type = type(my_array)
print(array_type)

#Data Type of a NumPy Array Containing Strings:
my_string_array = np.array(["apple", "banana", "cherry"])
string_array_type = type(my_string_array)
string_array_dtype = my_string_array.dtype
print(string_array_dtype)
