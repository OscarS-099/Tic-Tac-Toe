
class Game:

    EMPTY = " "
    DIM = 3
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
        string += f"1 {self._board[2][0]}|{self._board[2][1]}|{self._board[2][2]}\n"
        string += f"\n{self._player} turn to play"
        return string

    def play(self,row,col):
        row -= 1
        col -= 1
        self._board[row][col] = self._player
        self._player = Game.P2 if self._player is Game.P1 else Game.P1

    @property
    def winner(self):
        pass

if __name__ == "__main__":
    pass
