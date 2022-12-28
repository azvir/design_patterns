class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        # self.strength = 10
        # self.agility = 10
        # self.intelligence = 10
        self.stat = [10, 10, 10]

    @property
    def strength(self):
        return self.stat[Creature._strength]

    @strength.setter
    def strength(self, value):
        self.stat[Creature._strength] = value

    @property
    def agility(self):
        return self.stat[Creature._agility]

    @agility.setter
    def agility(self, value):
        self.stat[Creature._agility] = value

    @property
    def intelligence(self):
        return self.stat[Creature._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stat[Creature._intelligence] = value

    @property
    def max_stat(self):
        # return max(self.strength, self.agility, self.intelligence)
        return max(self.stat)

    @property
    def average_stat(self):
        # return sum(self.strength, self.agility, self.intelligence) / 3.0
        return sum(self.stat) / float(len(self.stat))
