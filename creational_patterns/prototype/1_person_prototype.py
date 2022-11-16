import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


if __name__ == '__main__':
    john = Person('John', Address('Legnicka 21b/1', 'Wroclaw', 'Poland'))
    print(john)
    print('---')

    # issue: jane object will reference to the same object as john.
    jane = john
    jane.name = 'Jane'
    print(john)
    print(jane)
    print('---')

    # issue: jane and john object refer to the same address object,
    # so modification of address object cause changes for both
    address = Address('Legnicka 21b/1', 'Wroclaw', 'Poland')
    john = Person('John', address)
    jane = Person('Jane', address)
    jane.address.street_address = 'Wesoła 30/4'
    print(john)
    print(jane)
    print('---')

    #
    john = Person('John', Address('Legnicka 21b/1', 'Wroclaw', 'Poland'))
    # copy.copy don't make copy of nested objects
    # jane = copy.copy(john)
    jane = copy.deepcopy(john)
    jane.name = 'Jane'
    jane.address.street_address = 'Wesoła 30/4'
    print(john)
    print(jane)
    print('---')
