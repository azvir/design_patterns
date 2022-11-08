# OCP - Open Closed Principle
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OCP - open for extension, closed for modification


class ProductFilter:
    @staticmethod
    def filter_by_color(_products, color):
        for _product in _products:
            if _product.color == color:
                yield _product

    @staticmethod
    def filter_by_size(_products, size):
        for _product in _products:
            if _product.size == size:
                yield _product

    @staticmethod
    def filter_by_color_and_size(_products, color, size):
        for _product in _products:
            if _product.color == color and _product.size == size:
                yield _product

# Specification


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item),
            self.args
        ))


class BaseFilter(Filter):
    def __init__(self):
        super().__init__()

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old):')
    for product in pf.filter_by_color(products, Color.GREEN):
        print(f'  - {product.name} is green')

    bf = BaseFilter()
    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for product in bf.filter(products, green):
        print(f'  - {product.name} is green')

    print('Large products (new):')
    large = SizeSpecification(Size.LARGE)
    for product in bf.filter(products, large):
        print(f'  - {product.name} is large')

    print('Large blue products:')
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpecification(Color.BLUE)
    for product in bf.filter(products, large_blue):
        print(f'  - {product.name} is large and blue')
