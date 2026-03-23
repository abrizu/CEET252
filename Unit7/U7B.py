import math

# U7A - Perimeter / Circumference calculation for Square, Rectangle, and Circle
class Square:
    def __init__(self, length):
        self.length = length

    def perimeter(self):
        return 4 * self.length

# add two classes here for Rectangle and Circle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

S1 = Square(2.55)
R1 = Rectangle(1.55, 3.45)
C1 = Circle(1.55)
print('Area of Square = ', format(S1.perimeter(), '.3f')) # output with 5 decimals --> change to 3 decimals
print('Area of Rectangle = ', format(R1.perimeter(), '.3f')) # output with 5 decimals --> change to 3 decimals
print('Area of Circle = ', format(C1.circumference(), '.3f')) # output with 5 decimals --> change to 3 decimals

# call the classes and print the results with 3 decimals
# use R1 = ...(1.55, 3.45), C1 = ...(1.55)
