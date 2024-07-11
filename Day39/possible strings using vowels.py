import itertools

def generate_all_strings(characters):
    permutations = itertools.permutations(characters)
    return [''.join(p) for p in permutations]

# Define the characters to use
characters = ['a', 'e', 'i', 'o', 'I']

# Generate all possible strings
all_strings = generate_all_strings(characters)

# Print the generated strings
for s in all_strings:
    print(s)
