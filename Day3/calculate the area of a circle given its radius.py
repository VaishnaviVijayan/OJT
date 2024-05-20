import math

def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * (radius ** 2)


radius = 5
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
