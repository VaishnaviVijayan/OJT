class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def display_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    print(f"Diagonal: {shape.diagonal()}")

# Example usage:
rect = Rectangle(3, 4)
square = Square(5)

display_info(rect)
display_info(square)
