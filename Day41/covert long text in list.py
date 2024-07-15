from collections import Counter
import re

def process_text(text):
    # Convert text to a list of words
    words = re.findall(r'\b\w+\b', text.lower())  # Using regex to extract words and convert to lower case

    # Count the frequency of each word
    word_count = Counter(words)

    # Print the list of words
    print("List of words:")
    print(words)
    print()

    # Print the frequency of each word
    print("Frequency of each word:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Example usage
long_text = """
Once upon a time, in a faraway land, there was a small village. The villagers were kind and hardworking.
They helped each other and lived in harmony. In this village, there was a wise old man who was respected
by everyone. He had a wealth of knowledge and often shared it with the villagers. One day, a young boy
came to the old man with a question. The old man listened carefully and then gave a thoughtful answer.
The boy thanked the old man and went on his way. The villagers continued to live their peaceful lives,
always remembering the wise words of the old man.
"""

process_text(long_text)
