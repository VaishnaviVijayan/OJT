import re

class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = self._validate_age(age)
        self.email = self._validate_email(email)

    def _validate_age(self, age: int) -> int:
        if isinstance(age, int) and age > 0:
            return age
        else:
            raise ValueError("Age must be a positive integer")

    def _validate_email(self, email: str) -> str:
        # Regular expression for validating an email
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        if email_regex.match(email):
            return email
        else:
            raise ValueError("Invalid email format")

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"

# Example usage:
try:
    person = Person("Alice", 30, "alice@example.com")
    print(person)
except ValueError as e:
    print(e)

try:
    invalid_person = Person("Bob", -5, "bob@example.com")
except ValueError as e:
    print(e)

try:
    invalid_person = Person("Charlie", 25, "invalid-email")
except ValueError as e:
    print(e)
