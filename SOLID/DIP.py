# Dependency Inversion Principle
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        ...


class Relationships(RelationshipBrowser):  # low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent_, child):
        self.relations.append(
            (parent_, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent_)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    """If you have dependency better to provide some utility methods right inside low-level module"""
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')
    def __init__(self, browser):
        for child in browser.find_all_children_of('John'):
            print(f'John has a child called {child}.')


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Sam')
    child2 = Person('Mati')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)
