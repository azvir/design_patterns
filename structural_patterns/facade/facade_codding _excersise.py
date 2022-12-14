"""

A magic square is a square matrix of numbers where the sum in each row, each column,
 and each of the diagonals is the same.

You are given a system of 3 classes that can be used to make a magic square. The classes are:

    Generator:this class generates a 1-dimensional list of random digits in range 1 to 9.

    Splitter:this class takes a 2D list and splits it into all possible arrangements of 1D lists.
             It gives you the columns, the rows and the two diagonals.

    Verifier:this class takes a 2D list and verifies that the sum of elements in every sublist is the same.

Please implement a Façade class called MagicSquareGenerator  which simply generates the magic square of a given size.
"""
from random import randint


class Generator:
    @staticmethod
    def generate(count):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    @staticmethod
    def split(array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    @staticmethod
    def verify(arrays):
        first_row_sum = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first_row_sum:
                return False

        return True


class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        magic_square = [self.generator.generate(size) for _ in range(size)]
        while not self.verifier.verify(self.splitter.split(magic_square)):
            magic_square = [self.generator.generate(size) for _ in range(size)]
        return magic_square


def test_generator():
    magic_square_generator = MagicSquareGenerator()
    assert Verifier().verify(magic_square_generator.generate(3))
