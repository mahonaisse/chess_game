from pieces import Pawn, Knight, Bishop, King, Queen, Rook, Position

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
            'a8': self.bRook1, 'b8': self.bKnight1, 'c8': self.bBishop1, 'd8': self.bQueen, 'e8': self.bKing, 'f8': self.bBishop2, 'g8': self.bKnight2, 'h8': self.bRook2,
            'a7': self.bPawn1, 'b7': self.bPawn2, 'c7': self.bPawn3, 'd7': self.bPawn4, 'e7': self.bPawn5, 'f7': self.bPawn6, 'g7': self.bPawn7, 'h7': self.bPawn8,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            'a2': self.wPawn1, 'b2': self.wPawn2, 'c2': self.wPawn3, 'd2': self.wPawn4, 'e2': self.wPawn5, 'f2': self.wPawn6, 'g2': self.wPawn7, 'h2': self.wPawn8,
            'a1': self.wRook1, 'b1': self.wKnight1, 'c1': self.wBishop1, 'd1': self.wQueen, 'e1': self.wKing, 'f1': self.wBishop2, 'g1': self.wKnight2, 'h1': self.wRook2
        }


    def get_piece_at_pos(self, user_pos):
        test_pos = Position(user_pos)
        return self.board[test_pos.get_cur_pos()]

    def move_piece(self, starting_pos, ending_pos, player):
        
        self.starting_piece = self.get_piece_at_pos(starting_pos) # identify starting piece
        self.ending_piece = self.get_piece_at_pos(ending_pos) # identify ending piece

        # Check all failing conditions. If there are no failing conditions, move the piece.
        if not self.starting_piece: # check if starting piece exists
            print('No piece at specified starting position')
            return False

        elif self.ending_piece and self.ending_piece.get_color() == self.starting_piece.get_color(): # check if ending position is an friendly occupied square
            print('You are trying to move into a friendly-occupied square.')
            return False

        elif self.ending_piece and self.ending_piece.get_color() != self.starting_piece.get_color() and ending_pos not in self.starting_piece.get_valid_takes(self): # check for invalid take
            print('You are trying to take a piece that you cannot take.')
            return False


        elif self.ending_piece and self.ending_piece.get_color() == self.starting_piece.get_color() and ending_pos not in self.starting_piece.get_valid_moves(self): # checks for invalid move
            print(f'{ending_pos} is not a valid move for {self.starting_piece}.')
            return False
        

        else: # passes all conditions, move the piece
            self.board[ending_pos] = self.board[starting_pos]
            self.board[starting_pos] = None
            self.starting_piece.set_position(ending_pos)
            if self.ending_piece: # taking enemy piece
                print(f'{self.starting_piece} moved from {starting_pos} to {ending_pos}, taking {self.ending_piece}.')
            else: # moving to empty square
                print(f'{self.starting_piece} moved from {starting_pos} to empty square at {ending_pos}.')