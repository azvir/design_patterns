from abc import ABC


class Expression(ABC):
    ...


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1), AdditionExpression(DoubleExpression(2),
                                                DoubleExpression(3))
    )
    buffer = []
    e.print(buffer)
    print(f"{''.join(buffer)} = {e.eval()}")
