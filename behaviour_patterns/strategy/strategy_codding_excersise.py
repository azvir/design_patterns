"""
Consider the quadratic equation and its canonical solution:

The part b^2-4*a*c is called the discriminant. Suppose we want to provide an API withi
 two different strategies for calculating the discriminant:

    In OrdinaryDiscriminantStrategy , If the discriminant is negative, we return it as-is.
     This is OK, since our main API returns Complex  numbers anyway.

    In RealDiscriminantStrategy , if the discriminant is negative, the return value is NaN (not a number).
     NaN propagates throughout the calculation, so the equation solver gives two NaN values.
      In Python, you make such a number with float('nan').

Please implement both of these strategies as well as the equation solver itself.
 With regards to plus-minus in the formula, please return the + result as the first element and - as the second.
  Note that the solve() method is expected to return complex values.

"""


from abc import ABC
import cmath
import math


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return (b**2) - (4 * a * c)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = ((b**2) - (4 * a * c))
        if d < 0:
            return float('nan')
        return d


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        d = self.strategy.calculate_discriminant(a, b, c)
        r1 = (-b + cmath.sqrt(d)) / (2 * a)
        r2 = (-b - cmath.sqrt(d)) / (2 * a)
        return r1, r2


def test_positive_ordinary():
    strategy = OrdinaryDiscriminantStrategy()
    solver = QuadraticEquationSolver(strategy)
    results = solver.solve(1, 10, 16)
    assert complex(-2, 0), results[0]
    assert complex(-8, 0), results[1]


def test_positive_real():
    strategy = RealDiscriminantStrategy()
    solver = QuadraticEquationSolver(strategy)
    results = solver.solve(1, 10, 16)
    assert complex(-2, 0), results[0]
    assert complex(-8, 0), results[1]


def test_negative_ordinary():
    strategy = OrdinaryDiscriminantStrategy()
    solver = QuadraticEquationSolver(strategy)
    results = solver.solve(1, 4, 5)
    assert complex(-2, 1), results[0]
    assert complex(-2, -1), results[1]


def test_negative_real():
    strategy = RealDiscriminantStrategy()
    solver = QuadraticEquationSolver(strategy)
    results = solver.solve(1, 4, 5)
    assert math.isnan(results[0].real)
    assert math.isnan(results[1].real)
    assert math.isnan(results[0].imag)
    assert math.isnan(results[1].imag)
