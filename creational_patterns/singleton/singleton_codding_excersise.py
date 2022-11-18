"""
Since implementing a singleton is easy, you have a different challenge: write a function called is_singleton().
This methld takes a factory method that returns an object and it's up to you to determine whether
 or not that object is a singleton instance.

"""
from copy import deepcopy


def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    return factory() is factory()


obj = [1, 2, 3]


def test_positive():
    assert is_singleton(lambda: obj)


def test_negative():
    assert not is_singleton(lambda: deepcopy(obj))
