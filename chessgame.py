class ChessGame:
    def __init__(self, whitePlayer, blackPlayer, board=Board()):
        self.white = whitePlayer
        self.black = blackPlayer
        self.board = board

class Player:
    pass

class Board:
    pass

class Position:
    def __init__(self, pos):
        self.rank = pos[1]
        self.file = pos[0]

    def output_pos(self):
        return f'{file}{rank}'