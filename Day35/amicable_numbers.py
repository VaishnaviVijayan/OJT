def sum_of_proper_divisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

def check_amicable_numbers(num1, num2):
    return (sum_of_proper_divisors(num1) == num2) and (sum_of_proper_divisors(num2) == num1)

# Example usage:
num1, num2 = 220, 284
if check_amicable_numbers(num1, num2):
    print(f"{num1} and {num2} are amicable numbers")
else:
    print(f"{num1} and {num2} are not amicable numbers")

num1, num2 = 1184, 1210
if check_amicable_numbers(num1, num2):
    print(f"{num1} and {num2} are amicable numbers")
else:
    print(f"{num1} and {num2} are not amicable numbers")
