# Interface Segregation Principle
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    def print(self, document):
        """OK"""
        pass

    def fax(self, document):
        pass  # no operation

    def scan(self, document):
        """Not supported"""
        raise NotImplementedError("Printer cannot scan!")


class Print:
    @abstractmethod
    def print(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class Scan:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Print):
    def print(self, document):
        pass


class Photocopier(Print, Scan):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Print, Scan):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


"""
So the interface aggregation principle states that you should segregate these, you should split them
into the smallest interfaces you can build so that people don't have to implement more than they need to.
"""


class MultiFunctionMachine(MultiFunctionDevice):
    def print(self, document):
        pass

    def scan(self, document):
        pass
