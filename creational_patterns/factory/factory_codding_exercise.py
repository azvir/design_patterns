"""
You are given a class called Person . The person has two attributes: id , and name .
Please implement a  PersonFactory that has a non-static  create_person()  method that takes a person's name
and return a person initialized with this name and an id.
The id of the person should be set as a 0-based index of the object created.
So, the first person the factory makes should have 'id=0', second 'id=1' and so on.

"""


class Person:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name


class PersonFactory:
    id = 0

    def create_person(self, name):
        person = Person(self.id, name)
        self.id += 1
        return person


def test_bob_has_index_0():
    pf = PersonFactory()
    person = pf.create_person('Bob')
    assert person.name == 'Bob'
    assert person.id == 0


def test_third_person_has_index_2():
    pf = PersonFactory()
    person1 = pf.create_person('Bob')
    person2 = pf.create_person('Marcin')
    person3 = pf.create_person('Sam')
    assert person3.id == 2
