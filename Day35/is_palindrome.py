def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Example usage:
num = 12321
if is_palindrome(num):
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")

num = 12345
if is_palindrome(num):
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")
