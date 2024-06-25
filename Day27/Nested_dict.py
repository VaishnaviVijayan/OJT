def get_nested_dict_value(nested_dict, path):
    
    # Split the path into components and remove the leading empty string caused by the leading '/'
    keys = path.strip("/").split("/")
    
    current_dict = nested_dict
    
    for key in keys:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            # If any key in the path doesn't exist, return None
            return None
    
    return current_dict

# Example usage:
file_system = {
    'home': {
        'user': {
            'documents': {
                'file1.txt': 'content1',
                'file2.txt': 'content2'
            },
            'pictures': {
                'photo1.jpg': 'content3',
                'photo2.jpg': 'content4'
            }
        }
    }
}

path = "/home/user/documents"
result = get_nested_dict_value(file_system, path)
print(result)
# Output: {'file1.txt': 'content1', 'file2.txt': 'content2'}

invalid_path = "/home/user/music"
result_invalid = get_nested_dict_value(file_system, invalid_path)
print(result_invalid)
# Output: None
