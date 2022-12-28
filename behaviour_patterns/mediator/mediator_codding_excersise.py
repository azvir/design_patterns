"""
Our system has any number of instances of Participant  classes.
 Each Participant has a value integer attribute, initially zero.

A participant can say()  a particular value, which is broadcast to all other participants.
 At this point in time, every other participant is obliged to increase their value  by the value being broadcast.

Example:

    Two participants start with values 0 and 0 respectively

    Participant 1 broadcasts the value 3. We now have Participant 1 value = 0, Participant 2 value = 3

    Participant 2 broadcasts the value 2. We now have Participant 1 value = 2, Participant 2 value = 3

"""


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.join(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


class Mediator:
    def __init__(self):
        self.participants = []

    def join(self, participant):
        self.participants.append(participant)

    def broadcast(self, who, value):
        for p in self.participants:
            if p != who:
                p.value += value


def test_broadcasting():
    m = Mediator()
    p1 = Participant(m)
    p2 = Participant(m)

    p1.say(3)
    assert p1.value == 0
    assert p2.value == 3

    p2.say(2)
    assert p1.value == 2
    assert p2.value == 3
