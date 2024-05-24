class MathOperations:
    @classmethod
    def addition(cls, num1, num2):
        return num1 + num2

    @classmethod
    def subtraction(cls, num1, num2):
        return num1 - num2

    @classmethod
    def multiplication(cls, num1, num2):
        return num1 * num2

    @staticmethod
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * MathOperations.factorial(num - 1)

# Example usage:
print("Addition:", MathOperations.addition(5, 3))
print("Subtraction:", MathOperations.subtraction(5, 3))
print("Multiplication:", MathOperations.multiplication(5, 3))
print("Factorial of 5:", MathOperations.factorial(5))
