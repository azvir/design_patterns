"""
Imagine a game where one or more rats can attack a player. Each individual rat has an initial attack value of 1.
However, rats attack as a swarm, so each rat's attack value is actually equal to the total number of rats in play.

Given that a rat enters play through the initializer and leaves play (dies) via its __exit__ method,
 please implement the Game and Rat classes so that, at any point in the game,
  the Attack value of a rat is always consistent.


"""
import pytest


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.rat_dies = Event()
        self.notify_rat = Event()


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1

        game.rat_enters.append(self.rat_enters)
        game.notify_rat.append(self.notify_rat)
        game.rat_dies.append(self.rat_dies)

        self.game.rat_enters(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_dies(self)

    def rat_enters(self, which_rat):
        if which_rat != self:
            self.attack += 1
            self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if which_rat == self:
            self.attack += 1

    def rat_dies(self, which_rat):
        self.attack -= 1


@pytest.fixture
def game():
    return Game()


def test_single_rat(game):
    rat = Rat(game)
    assert rat.attack == 1


def test_two_rats(game):
    rat = Rat(game)
    rat2 = Rat(game)
    assert rat.attack == 2
    assert rat2.attack == 2


def test_three_rats_one_dies(game):
    rat = Rat(game)
    assert rat.attack == 1

    rat2 = Rat(game)
    assert rat.attack == 2
    assert rat2.attack == 2

    with Rat(game) as rat3:
        assert rat.attack == 3
        assert rat2.attack == 3
        assert rat3.attack == 3

    assert rat.attack == 2
    assert rat2.attack == 2