def string_to_int(s):
    """
    Converts a string to an integer.
    
    Parameters:
    s (str): The string to convert.
    
    Returns:
    int: The converted integer, or None if conversion fails.
    """
    try:
        result = int(s)
        return result
    except ValueError:
        print(f"Error: '{s}' is not a valid integer.")
        return None
    except TypeError:
        print("Error: Input must be a string.")
        return None

def main():
    strings = ["123", "abc", "45.67", None]
    
    for s in strings:
        print(f"Converting '{s}':")
        result = string_to_int(s)
        if result is not None:
            print(f"Successfully converted to integer: {result}")
        print()


