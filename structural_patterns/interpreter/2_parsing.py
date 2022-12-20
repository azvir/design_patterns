from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPARENTH = auto()
        RPARENTH = auto()

    def __init__(self, type_, text):
        self.type = type_
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input_):
    result = []
    i = 0

    while i < len(input_):
        match(char := input_[i]):
            case '+':
                result.append(Token(Token.Type.PLUS, char))
            case '-':
                result.append(Token(Token.Type.MINUS, char))
            case '(':
                result.append(Token(Token.Type.LPARENTH, char))
            case ')':
                result.append(Token(Token.Type.RPARENTH, char))
            case _:
                next_ = i + 1
                digit = [input_[i]]
                while next_ < len(input_):
                    next_char = input_[next_]
                    if next_char.isdigit():
                        digit.append(next_char)
                        next_ += 1
                        i += 1
                    else:
                        break
                result.append(Token(Token.Type.INTEGER, ''.join(digit)))
        i += 1
    return result


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Operation(Enum):
        ADDITION = 1
        SUBTRACTION = 2

    def __init__(self):
        self.operation = None
        self.left = None
        self.right = None

    @property
    def value(self):
        match self.operation:
            case BinaryExpression.Operation.ADDITION:
                return self.left.value + self.right.value
            case BinaryExpression.Operation.SUBTRACTION:
                return self.left.value - self.right.value
            case _:
                raise Exception("Not known operation")


def parse(tokens):
    result = BinaryExpression()
    have_lhs = False

    i = 0
    while i < len(tokens):
        token = tokens[i]

        match token.type:
            case Token.Type.INTEGER:
                integer = Integer(int(token.text))
                if not have_lhs:
                    result.left = integer
                    have_lhs = True
                else:
                    result.right = integer
            case Token.Type.PLUS:
                result.operation = BinaryExpression.Operation.ADDITION
            case Token.Type.MINUS:
                result.operation = BinaryExpression.Operation.SUBTRACTION
            case Token.Type.LPARENTH:
                j = i
                while j < len(tokens):
                    if tokens[j].type == Token.Type.RPARENTH:
                        break
                    j += 1
                subexpression = tokens[i+1:j]
                element = parse(subexpression)
                if not have_lhs:
                    result.left = element
                    have_lhs = True
                else:
                    result.right = element
                i = j
        i += 1
    return result


def calc(input_):
    tokens = lex(input_)
    parsed = parse(tokens)
    return f'{input_} = {parsed.value}'


def test_lexical_interpretation():
    expected = '(14+12)+(19-5) = 40'
    assert calc('(14+12)+(19-5)') == expected
