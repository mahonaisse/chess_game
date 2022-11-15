class Piece:
    def __init__(self, piece_pos, color):
        self.position = position(piece_pos)
        self.color = color
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

    def change_position(new_position):
        self.position = position(new_pos)

class Pawn(Piece):
    def get_valid_moves(self):
        # if color is black multiply all possible positions by -1
        if self.color == 'W':
            return self.position.get_directional(2) # a white pawn can move forward
        elif self.color == 'B':
            return self.position.get_directional(6) # a black pawn can move backwards


class Knight(Piece):
    pass

class Biship(Piece):
    pass

class King(Piece):
    pass

class Queen(Piece):
    pass

class Rook(Piece):
    pass