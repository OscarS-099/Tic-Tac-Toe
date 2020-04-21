from abc import ABC, abstractmethod
from Game import Game, GameError

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            print(self._game)
            try:
                row = int(input("Which row? "))
                col = int(input("Which column? "))
            except ValueError:
                print("Row and Column need to be numbers, try again")
                while True:
                    try:
                        row = int(input("Which row? "))
                        col = int(input("Which column? "))
                        break
                    except:
                        continue

            try:
                self._game.play(row,col)
            except GameError as e:
                print(f"GameError: {e}")
                while True:
                    try:
                        row = int(input("Which row? "))
                        col = int(input("Which column? "))
                        self._game.play(row,col)
                        break
                    except:
                        continue


        print(self._game)
        print(f"The winner was {self._game.winner}")

if __name__ == "__main__":
    ui = Terminal()
    ui.run()
