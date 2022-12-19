"""
Chain of Responsibility Coding Exercise

You are given a game scenario with classes Goblin and GoblinKing. Please implement the following rules:

    A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.
    When the Goblin King is in play, every other goblin gets +1 Attack.
    Goblins get +1 to Defense for every other Goblin in play (a GoblinKing is a Goblin!).

Example:

    Suppose you have 3 ordinary goblins in play. Each one is a 1/3 (1/1 + 0/2 defense bonus).
    A goblin king comes into play.
     Now every goblin is a 2/4 (1/1 + 0/3 defense bonus from each other + 1/0 from goblin king)

The state of all the goblins has to be consistent as goblins are added and removed from the game.
Here is an example of the kind of test that will be run on the system:

    class FirstTestSuite(unittest.TestCase):
        def test(self):
            game = Game()
            goblin = Goblin(game)
            game.creatures.append(goblin)

            self.assertEqual(1, goblin.attack)
            self.assertEqual(1, goblin.defense)

Note: creature removal (unsubscription) does not need to be implemented.
"""
from abc import ABC
from enum import Enum


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature, what_to_query, default_value):
        self.value = default_value
        self.creature = creature
        self.what_to_query = what_to_query


class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.name = None
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        ...

    @property
    def defense(self):
        ...

    def query(self):
        ...


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)
        self.name = 'Goblin'

    @property
    def attack(self):
        q = Query(self, WhatToQuery.ATTACK, self.initial_attack)
        for creature in self.game.creatures:
            creature.query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self, WhatToQuery.DEFENSE, self.initial_defense)
        for creature in self.game.creatures:
            creature.query(self, q)
        return q.value

    def query(self, sender, query):
        if self != sender and WhatToQuery.DEFENSE == query.what_to_query:
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, game, attack=3, defense=3):
        super().__init__(game, attack, defense)
        self.name = 'GoblinKing'

    def query(self, sender, query: Query):
        if self != sender and WhatToQuery.ATTACK == query.what_to_query:
            query.value += 1
        else:
            super().query(sender, query)


class Game:
    def __init__(self):
        self.creatures = []


def test_1_goblin_in_game():
    game = Game()
    goblin = Goblin(game)
    game.creatures.append(goblin)

    assert 1 == goblin.attack
    assert 1 == goblin.defense

    goblin2 = Goblin(game)
    game.creatures.append(goblin2)

    assert 1 == goblin.attack
    assert 2 == goblin.defense

    goblin_king = GoblinKing(game)
    game.creatures.append(goblin_king)

    assert 2 == goblin.attack
    assert 3 == goblin.defense
