# Polygon Area Calculator
from math import sqrt, pow


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width**2) + (self.height**2)) ** 0.5
        # return sqrt(pow(self.width, 2) + pow(self.height, 2))

    # generate string representation of using '*'
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return "\n".join([f"{'*' * self.width}" for _ in range(self.height)]) + "\n"

    # Calculate how many times a given shape can fit inside the current shape
    # shape param is instance of that shape (Rectangle, Square, etc.)
    def get_amount_inside(self, shape):
        rect_area = self.get_area()
        shape_area = shape.get_area()
        return rect_area // shape_area


class Square(Rectangle):
    def __init__(self, side):
        # self.width = side
        # self.height = side
        # same as, but using super() allows you to call the parent class's methods
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
