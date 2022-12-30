class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def can_vote(self):
        return self.age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value != self.age:

            old_can_vote = self.can_vote

            self._age = value
            self.property_changed('age', value)

            if old_can_vote != self.can_vote:
                self.property_changed('can_vote', self.can_vote)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        self.person.property_changed.append(self.control_person)

    def control_person(self, attr, value):
        match attr:
            case 'age':
                if value < 16:
                    print("You still cannot drive")
                else:
                    print("You can drive now")
                    self.person.property_changed.remove(self.control_person)


def person_changed(attr, value):
    if attr == 'can_vote':
        print(f'Voting ability changed to {value}')


if __name__ == '__main__':

    p = Person(age=12)
    p.property_changed.append(person_changed)

    for age in range(14, 20):
        print(f'Settings age to {age}')
        p.age = age
