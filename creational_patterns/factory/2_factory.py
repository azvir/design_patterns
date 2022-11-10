from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = PointFactory.new_polar_point(1, 3)
    p2 = Point.PointFactory().new_polar_point(1, 3)
    p3 = Point.factory.new_polar_point(1, 3)
    print(p1, p2, p3, sep='\n')
