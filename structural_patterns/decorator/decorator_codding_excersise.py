"""

You are given two types, Circle and Square, and a decorator called ColoredShape.

The decorator adds the color to the string output for a given shape, just as we did in the lecture.

There's a trick though: the decorator now has a resize() method that should resize the underlying shape. However,
 only the Circle has a resize() method; the Square does not — do not add it!

You are asked to complete the implementation of Circle, Square and ColoredShape.

Here is a sample unit test that should pass:

    class Evaluate(TestCase):
      def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual(
          'A circle of radius 5 has the color red',
          str(circle)
        )
        circle.resize(2)
        self.assertEqual(
          'A circle of radius 10 has the color red',
          str(circle)
        )
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return 'A circle of radius %s' % self.radius

class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'A square with side %s' % self.side

class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        if isinstance(self.shape, Square):
            return
        self.shape.resize(factor)

    def __str__(self):
        return '{} has the color {}'.format(self.shape, self.color)


def test_circle():
    assert "A circle of radius 5 has the color red" == str(ColoredShape(Circle(5), 'red'))


def test_circle_resize():
    circle = ColoredShape(Circle(7), 'green')
    circle.resize(2)
    assert "A circle of radius 14 has the color green" == str(circle)


def test_square():
    square = ColoredShape(Square(4), 'blue')
    square.resize(2)
    assert "A square with side 4 has the color blue" == str(square)
