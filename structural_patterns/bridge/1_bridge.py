# circle square
# vector raster
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        ...
    
    def render_square(self, side):
        ...
    

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')
        
        
class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')
        

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        ...

    def resize(self, factor):
        ...


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(radius=self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()

    print('\n\n Vector drawing')
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    print('\n\n Raster drawing')
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

