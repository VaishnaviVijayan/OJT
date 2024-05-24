class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
if __name__ == "__main__":
    rect = Rectangle(6, 2)
    print("Area:", rect.calculate_area())
    print("Perimeter:", rect.calculate_perimeter())
