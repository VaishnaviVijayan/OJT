def remove_every_third(numbers):
    index = 2  # The third element has index 2
    while numbers:
        # Wrap around the index if it exceeds the list length
        index = index % len(numbers)
        # Print and remove the element at the current index
        print(f"Removing: {numbers.pop(index)}")
        # Move to the next third element
        index += 2

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_every_third(numbers)
