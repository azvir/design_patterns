import string
import random
import sys


class User:
    def __init__(self, full_name):
        self.full_name = full_name

    def __str__(self):
        return self.full_name


class MemoryOptimizedUser:
    strings_cache = []

    def __init__(self, full_name):
        def get_or_add(str_):
            if str_ not in self.strings_cache:
                MemoryOptimizedUser.strings_cache.append(str_)
            return MemoryOptimizedUser.strings_cache.index(str_)

        self.full_name = [get_or_add(name) for name in full_name.split(' ')]

    def __str__(self):
        return ' '.join(MemoryOptimizedUser.strings_cache[index] for index in self.full_name)


def generate_string(length):
    letters = string.ascii_lowercase
    return ''.join([random.choice(letters) for _ in range(length)])


if __name__ == '__main__':

    first_names = [generate_string(8) for _ in range(10)]
    last_names = [generate_string(8) for _ in range(10)]

    full_names = [f'{random.choice(first_names)} {random.choice(last_names)}' for _ in range(1_000)]

    print('=== users1 - not optimised ===\n')
    users = [User(full_name) for full_name in full_names]
    print(f'users list contains: {len(users)}')
    print(f'users object has size: {sys.getsizeof(users)} bytes')
    print(f'first user: "{users[0]}"')

    print('\n\n=== users2 - optimised ===\n')
    users2 = [MemoryOptimizedUser(full_name) for full_name in full_names]
    print(f'users2 list contains: {len(users2)}')
    print(f'users2 object has size: {sys.getsizeof(users2)} bytes')
    print(f'first user: "{users2[0]}"')
