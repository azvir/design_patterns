from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def __init__(self):
        super().__init__()

    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'

    def __iter__(self):
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count
        for i in range(0, count):
            self.append(Neuron(f'{name}-{i}'))

    def __str__(self):
        return f'{self.name} with {self.count} neurons'


if __name__ == '__main__':
    n1 = Neuron('N1')
    n2 = Neuron('N2')

    l1 = NeuronLayer('L1', 3)
    l2 = NeuronLayer('L2', 7)

    n1.connect_to(n2)
    n1.connect_to(l1)
    l1.connect_to(n2)
    l1.connect_to(l2)
    print(n1)
    print(n2)
    print(l1)
    print(l2)
