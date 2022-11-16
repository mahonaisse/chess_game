from pieces import Pawn, Knight, Bishop, King, Queen, Rook
class ChessGame:
    def __init__(self, whitePlayer, blackPlayer):
        self.white = whitePlayer
        self.black = blackPlayer
        self.board = Board()

class Player:
    pass

class Board:
    def __init__(self):
        # black pieces
        self.bRook1 = Rook('a8', 'B')
        self.bKnight1 = Knight('b8', 'B')
        self.bBishop1 = Bishop('c8', 'B')
        self.bQueen = Queen('d8', 'B')
        self.bKing = King('e8', 'B')
        self.bBishop2 = Bishop('f8', 'B')
        self.bKnight2 = Knight('g8', 'B')
        self.bRook2 = Rook('h8', 'B')

        # black pawns
        self.bPawn1 = Pawn('a7', 'B')
        self.bPawn2 = Pawn('b7', 'B')
        self.bPawn3 = Pawn('c7', 'B')
        self.bPawn4 = Pawn('d7', 'B')
        self.bPawn5 = Pawn('e7', 'B')
        self.bPawn6 = Pawn('f7', 'B')
        self.bPawn7 = Pawn('g7', 'B')
        self.bPawn8 = Pawn('h7', 'B')

        # white pieces
        self.wRook1 = Rook('a8', 'W')
        self.wKnight1 = Knight('b8', 'W')
        self.wBishop1 = Bishop('c8', 'W')
        self.wQueen = Queen('d8', 'W')
        self.wKing = King('e8', 'W')
        self.wBishop2 = Bishop('f8', 'W')
        self.wKnight2 = Knight('g8', 'W')
        self.wRook2 = Rook('h8', 'W')

        # white pawns
        self.wPawn1 = Pawn('a2', 'W')
        self.wPawn2 = Pawn('b2', 'W')
        self.wPawn3 = Pawn('c2', 'W')
        self.wPawn4 = Pawn('d2', 'W')
        self.wPawn5 = Pawn('e2', 'W')
        self.wPawn6 = Pawn('f2', 'W')
        self.wPawn7 = Pawn('g2', 'W')
        self.wPawn8 = Pawn('h2', 'W')

        # initial board
        self.board = {
            'a8': None, 'b8': None, 'c8': None, 'd8': None, 'e8': None, 'f8': None, 'g8': None, 'h8': None,
            'a7': None, 'b7': None, 'c7': None, 'd7': None, 'e7': None, 'f7': None, 'g7': None, 'h7': None,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            'a2': None, 'b2': None, 'c2': None, 'd2': None, 'e2': None, 'f2': None, 'g2': None, 'h2': None,
            'a1': None, 'b1': None, 'c1': None, 'd1': None, 'e1': None, 'f1': None, 'g1': None, 'h1': None
        }
