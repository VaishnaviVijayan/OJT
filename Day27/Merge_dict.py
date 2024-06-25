def merge_dictionaries(dict1, dict2):

    # Start with a copy of the first dictionary
    merged_dict = dict1.copy()
    
    # Update the merged dictionary with key-value pairs from the second dictionary
    merged_dict.update(dict2)
    
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)
# Output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
