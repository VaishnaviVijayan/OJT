import random

def generate_random_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

# Example usage:
random_number = generate_random_number()
print(f"The random number generated is: {random_number}")
