# Strongly not recommended

class CEO:
    _shared_data = {
        'name': 'Steve',
        'age': '55'
    }

    def __init__(self):
        self.__dict__ = self._shared_data

    def __str__(self):
        return f'{self.name} id {self.age} years old.'


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} managed ${self.money_managed}'


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    ceo2.name = 'Patric'
    ceo2.age = '40'
    print(ceo1, ceo2, sep='\n')
    print('-' * 50)

    cfo1 = CFO()
    cfo1.name = 'John'
    cfo1.money_managed = 103
    print(cfo1)
    cfo2 = CFO()
    cfo2.name = 'Marko'
    cfo2.money_managed = 402
    print(cfo1, cfo2, sep='\n')
