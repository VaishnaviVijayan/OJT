def all_unique_numbers(sequence):
    return len(sequence) == len(set(sequence))

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(all_unique_numbers(numbers))  # Output: True

numbers = [1, 2, 3, 4, 5, 1]
print(all_unique_numbers(numbers))  # Output: False
