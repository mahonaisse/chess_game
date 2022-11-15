class ChessGame:
    def __init__(self, whitePlayer, blackPlayer):
        self.white = whitePlayer
        self.black = blackPlayer
        self.board = Board()

class Player:
    pass

class Board:
    def __init__(self):
        pass

class Position:
    def __init__(self, pos):
        self.FILE_TO_NUM = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        self.NUM_TO_FILE = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        self.VALID_POSITIONS = {
            'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
        }

        self.rank = int(pos[1])
        self.file = self.FILE_TO_NUM[pos[0]]

    def output_pos(self, file, rank):
        return f'{self.NUM_TO_FILE[file]}{rank}'

    def __str__(self):
        return self.output_pos(self.file, self.rank)

    def get_directional(self, direction):
        if direction == 1:
            return self.output_pos(self.file-1, self.rank+1) if (self.file > 1 and self.rank < 8) else None # forward left
        elif direction == 2:
            return self.output_pos(self.file, self.rank+1) if self.rank < 8 else None # forward
        elif direction == 3:
            return self.output_pos(self.file+1, self.rank+1) if (self.file < 8 and self.rank) < 8 else None # forward right
        elif direction == 4: 
            return self.output_pos(self.file+1, self.rank) if self.file < 8 else None # right
        elif direction == 5:
            return self.output_pos(self.file+1, self.rank-1) if (self.file < 8 and self.rank > 1) else None # back right
        elif direction == 6:
            return self.output_pos(self.file, self.rank-1) if self.rank > 1 else None # back
        elif direction == 7:
            return self.output_pos(self.file-1, self.rank-1) if (self.file > 1 and self.rank > 1) else None # back left
        elif direction == 8:
            return self.output_pos(self.file-1, self.rank) if self.file > 1 else None # left