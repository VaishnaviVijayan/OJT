import math

def calculate_square_root(number):
    """Calculate the square root of a given number using the math module."""
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(number)

# Example usage:
number = 25
result = calculate_square_root(number)
print(f"The square root of {number} is {result}")
