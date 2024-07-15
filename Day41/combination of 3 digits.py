import itertools

def generate_three_digit_combinations():
    digits = list(range(10))  # Digits from 0 to 9
    combinations = list(itertools.combinations(digits, 3))
    return combinations

# Example usage
combinations = generate_three_digit_combinations()
print("All possible combinations of 3 digits:")
for combination in combinations:
    print(combination)
