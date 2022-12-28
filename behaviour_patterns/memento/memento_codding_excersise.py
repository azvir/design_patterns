import copy

import pytest


class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        m = Memento(copy.deepcopy(self.tokens))
        return m

    def revert(self, memento):
        self.tokens = memento


@pytest.fixture
def tm():
    return TokenMachine()


def test_single_token(tm):
    m = tm.add_token_value(123)
    tm.add_token_value(456)
    tm.revert(m)
    assert len(tm.tokens) == 1, 'We expect exactly 1 token'
    assert tm.tokens[0].value, 'The first token\'s value should be 123'


def test_two_tokens(tm):
    tm.add_token_value(1)
    m = tm.add_token_value(2)
    tm.add_token_value(3)
    tm.revert(m)
    assert len(tm.tokens) == 2, 'We should have exactly 2 tokens'
    assert tm.tokens[0].value == 1, 'First token should have value 1, you got ' + str(tm.tokens[0].value)
    assert tm.tokens[1].value == 2, 'Second token should have the value 2'


def test_fiddled_token(tm):
    token = Token(111)
    print('Made a token with value 111 and kept a reference')

    tm.add_token(token)
    print('Added this token to the list')

    m = tm.add_token_value(222)
    print('Added token 222 and kept a memento')

    print('Changed 111 token\'s value to 333... pay attention!')
    token.value = 333

    tm.revert(m)

    assert len(tm.tokens) == 2,\
        'At this point, token machine should have exactly 2 tokens, you have ' + str(len(tm.tokens))

    assert tm.tokens[0].value == 111,\
        'You got the tokens[0] value wrong here. Hint: did you init the memento by value?'
    