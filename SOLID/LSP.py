# Liskov Substitution Principle

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        self._size = size
        Rectangle.__init__(self, size, size)

    # violate the risk of LSP
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    # violate the risk of LSP
    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected_area = w * 10
    print(f"Expected an area of {expected_area}, got {rc.area}")


rect = Rectangle(2, 3)
use_it(rect)

sq = Square(5)
use_it(sq)

"""
How to correct it? 

- No need Square class, implement bool property to the Rectangle class to indicate square
- Factory method which would make a square instead of rectangle
"""
