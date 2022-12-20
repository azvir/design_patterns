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


def calc(input_):
    tokens = lex(input_)
    return ' '.join(map(str, tokens))


def test_lexical_interpretation():
    expected = '`(` `14` `+` `12` `)` `+` `(` `19` `-` `1` `)` `+` `5` `-` `1`'
    assert expected == calc('(14+12)+(19-1)+5-1')
