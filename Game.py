from itertools import product

class GameError(Exception):
    pass

class Game:

    EMPTY = " "
    DIM = 3
    DRAW = "Draw"
    P1 = "o"
    P2 = "x"

    def __init__(self):
        self._board = [[Game.EMPTY for _ in range(Game.DIM)] for _ in range(Game.DIM)]
        self._player = Game.P1

    def __repr__(self):
        string = "  1 2 3\n"
        string += f"1 {self._board[0][0]}|{self._board[0][1]}|{self._board[0][2]}\n"
        string += "  -----\n"
        string += f"2 {self._board[1][0]}|{self._board[1][1]}|{self._board[1][2]}\n"
        string += "  -----\n"
        string += f"3 {self._board[2][0]}|{self._board[2][1]}|{self._board[2][2]}\n"
        string += f"\n{self._player} turn to play"
        return string

    def play(self,row,col):
        row -= 1
        col -= 1

        if not (0 <= row < Game.DIM):
            raise GameError(f"Row {row + 1} not in range")
        if not (0 <= col < Game.DIM):
            raise GameError(f"Column {col + 1} not in range")

        if self._board[row][col] is not Game.EMPTY:
            raise GameError(f"Board not empty at {row + 1} {col + 1}")

        self._board[row][col] = self._player
        self._player = Game.P2 if self._player is Game.P1 else Game.P1

    def at(self,row,col):
        row -= 1
        col -= 1
        return self._board[row][col]

    @property
    def winner(self):
        for p in [Game.P1,Game.P2]:
            for row in range(Game.DIM):
                if all(self._board[row][col] is p for col in range(Game.DIM)):
                    return p
            for col in range(Game.DIM):
                if all(self._board[row][col] is p for row in range(Game.DIM)):
                    return p
                # Diagonals
                if all(self._board[i][i] is p for i in range(Game.DIM)):
                    return p
                if all(self._board[i][2-i] is p for i in range(Game.DIM)):
                    return p

        # Draw
        if all(self._board[row][col] is not Game.EMPTY for (row,col) in product(range(3),range(3))):
            return Game.DRAW

        # No winner
        return None

if __name__ == "__main__":
    pass
