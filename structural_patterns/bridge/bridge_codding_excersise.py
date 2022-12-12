"""

You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

Please refactor this hierarchy, giving the base class Shape  a constructor that takes an interface Renderer  defined as

    class Renderer(ABC):
        @property
        def what_to_render_as(self):
            return None

as well as VectorRenderer  and RasterRenderer  classes.
Each inheritor of the Shape  abstract class should have a constructor that takes a Renderer  such that,
 subsequently, each constructed object's __str__()  operates correctly, for example,

str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"
"""

from abc import ABC


class Shape(ABC):
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as}'


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'


def test_triangle_vector():
    assert "Drawing Triangle as lines" == str(Triangle(VectorRenderer()))


def test_square_raster():
    assert "Drawing Square as pixels" == str(Square(RasterRenderer()))
