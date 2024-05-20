from functools import reduce

# Define the lambda function to multiply two numbers
multiply = lambda x, y: x * y

# Define the function to calculate factorial using reduce
def factorial(n):
    if n < 0:
        raise ValueError("The factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return reduce(multiply, range(1, n + 1))

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
