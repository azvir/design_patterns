"""
Imagine a typical collectible card game which has cards representing creatures.
Each creature has two values: Attack and Health.
Creatures can fight each other, dealing their Attack damage, thereby reducing their opponent's health.

The class CardGame implements the logic for two creatures fighting one another. However,
the exact mechanics of how damage is dealt is different:

    TemporaryCardDamage : In some games (e.g., Magic: the Gathering),
     unless the creature has been killed, its health returns to the original value at the end of combat.

    PermanentCardDamage : In other games (e.g., Hearthstone), health damage persists.

You are asked to implement classes TemporaryCardDamageGame  and PermanentCardDamageGame
that would allow us to simulate combat between creatures.

Some examples:

    With temporary damage, creatures 1/2 and 1/3 can never kill one another.
     With permanent damage, second creature will win after 2 rounds of combat.

    With either temporary or permanent damage, two 2/2 creatures kill one another.
"""


from abc import ABC, abstractmethod


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]
        self.hit(c1, c2)
        self.hit(c2, c1)
        if (c1.health <= 0 and c2.health <= 0) or (c1.health > 0 and c2.health > 0):
            return -1
        elif c1.health <= 0:
            return c2_index
        elif c2.health <= 0:
            return c1_index

    @abstractmethod
    def hit(self, attacker, defender): ...


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        original_health = defender.health
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = original_health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack


def test_impasse():
    c1 = Creature(1, 2)
    c2 = Creature(1, 2)
    game = TemporaryDamageCardGame([c1, c2])
    assert game.combat(0, 1) == -1, 'Combat should yield -1 since nobody died.'
    assert game.combat(0, 1) == -1, 'Combat should yield -1 since nobody died.'


def test_temporary_murder():
    c1 = Creature(1, 1)
    c2 = Creature(2, 2)
    game = TemporaryDamageCardGame([c1, c2])
    assert game.combat(0, 1) == 1


def test_double_murder():
    c1 = Creature(2, 1)
    c2 = Creature(2, 2)
    game = TemporaryDamageCardGame([c1, c2])
    assert game.combat(0, 1) == -1


def test_permanent_damage_death():
    c1 = Creature(1, 2)
    c2 = Creature(1, 3)
    game = PermanentDamageCardGame([c1, c2])
    assert game.combat(0, 1) == -1, 'Nobody should win this battle.'
    assert c1.health == 1
    assert c2.health == 2
    assert game.combat(0, 1) == 1, 'Creature at index 1 should win this'
