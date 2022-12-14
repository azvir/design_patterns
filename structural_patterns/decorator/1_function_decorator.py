import time
from random import randint


def time_it(func):
    def wrapped():
        start = time.time()
        res = func()
        end = time.time()
        print(f'Function "{func.__name__}" takes {int((end - start)) * 1000}ms')
        return res
    return wrapped


@time_it
def some_op():
    print('Start operation')
    time.sleep(randint(1, 10))
    print('Operation done!')
    return 123


if __name__ == '__main__':
    some_op()
    time_it(some_op)()
