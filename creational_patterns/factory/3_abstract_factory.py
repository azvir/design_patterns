from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        ...


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        ...


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


#  better to create class like bellow
def make_drink(drink):
    if drink == 'tea':
        return TeaFactory().prepare(200)
    elif drink == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        print('Can\'t make it')
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        TEA = auto()
        COFFEE = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for count, f in enumerate(self.factories):
            print(count, f[0])
        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input('Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    # entry = input("What kind of drink would you like?\n")
    # drink = make_drink(entry)

    hot_drink = HotDrinkMachine().make_drink()
    if hot_drink:
        hot_drink.consume()
