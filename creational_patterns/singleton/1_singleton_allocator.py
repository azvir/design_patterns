import random


class Database:
    __instance = None

    def __init__(self):
        _id = random.randint(1, 100)
        print('object id = ', id(self))
        print('random id = ', _id)
        print()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


def test_object_the_same():
    d1 = Database()
    d2 = Database()
    assert d1 == d2


if __name__ == '__main__':
    # init will be run for every instance creation but for the same object
    d1 = Database()
    d2 = Database()
