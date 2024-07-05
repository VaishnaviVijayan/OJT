def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def check_strong_number(num):
    # Convert the number to a string to iterate over each digit
    num_str = str(num)
    # Calculate the sum of the factorial of each digit
    sum_of_factorials = sum(factorial(int(digit)) for digit in num_str)
    # Check if the sum of the factorials is equal to the original number
    return sum_of_factorials == num

# Example usage:
num = 145
if check_strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")

num = 123
if check_strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
