from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins!')

    @abstractmethod
    def start(self): ...

    @abstractmethod
    def take_turn(self): ...

    @property
    @abstractmethod
    def have_winner(self): ...

    @property
    @abstractmethod
    def winning_player(self): ...


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turn = 10
        self.turn = 1

    def start(self):
        print(f'Starting a game of chess with {self.number_of_players} players')

    def take_turn(self):
        print(f'Turn {self.turn} taken by {self.current_player}')
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def have_winner(self):
        return self.max_turn == self.turn

    @property
    def winning_player(self):
        return self.current_player


if __name__ == '__main__':
    chess_game = Chess()
    chess_game.run()
