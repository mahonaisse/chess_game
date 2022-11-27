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
    
    def get_cur_pos(self):
        return self.output_pos(self.file, self.rank)

    def output_pos(self, file, rank):
        return f'{self.NUM_TO_FILE[file]}{rank}'

    def __str__(self):
        return self.output_pos(self.file, self.rank)

    def get_directional(self, vertical_movement, horizontal_movement):
        # print('    ', vertical_movement, horizontal_movement)
        self.temp_rank = self.rank + vertical_movement
        self.temp_file = self.file + horizontal_movement
        # print(self.temp_file, self.temp_rank)
        if 0 < self.temp_rank < 9 and 0 < self.temp_file < 9:
            return self.output_pos(self.temp_file, self.temp_rank)
        else:
            return None

class Piece:
    def __init__(self, piece_pos, color):
        self.position = Position(piece_pos)
        self.color = 'White' if color == 'W' else 'Black'
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

    def __str__(self):
        return f'{self.color} {self.__class__.__name__ } at {self.position}'

    def set_position(self, new_pos):
        self.position = Position(new_pos)

    def get_name(self):
        return f'{self.color} {self.__class__.__name__} at {self.position}'

    def get_color(self):
        return self.color

class Pawn(Piece):
    def get_valid_moves(self, board):
        self.directions = []
        if self.color == 'White': # white pawns can move forward
            self.directions.append((1, 0))
        elif self.color == 'Black': # black pawns can move backward
            self.directions.append((-1, 0))

        # print(self.directions)
        # TODO: add more directions based on if there is a piece in that location the pawn can take. Pass the board as a parameter, maybe with a getter function to identify the piece at that position. 
        self.valid_moves = []
        for vertical_move, horizontal_move in self.directions:
            # print(vertical_move, horizontal_move)
            new_position = self.position.get_directional(vertical_move, horizontal_move)
            # print(new_position)
            if not board.get_piece_at_pos(new_position):
                self.valid_moves.append(new_position)
        # print(self.directions)
        # print(self.valid_moves)
        return self.valid_moves

    def get_valid_takes(self, board):
        self.directions = []
        if self.color == 'White':
            self.directions.extend([(1, -1), (1, 1)])
        elif self.color == 'Black':
            self.directions.extend([(-1, -1), (-1, 1)])
        # print(self.directions)
        self.valid_moves = []
        for vertical_move, horizontal_move in self.directions:
            new_position = self.position.get_directional(vertical_move, horizontal_move)
            # print(new_position)
            self.valid_moves.append(new_position)
        # print(self.valid_moves)
        return self.valid_moves


class Knight(Piece):
    def get_valid_moves(self, board):
        self.directions = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1)]
        self.valid_moves = []
        for vertical_move, horizontal_move in self.directions:
            new_position = self.position.get_directional(vertical_move, horizontal_move)
            if new_position and not board.get_piece_at_pos(new_position):
                self.valid_moves.append(new_position)

        return self.valid_moves

    def get_valid_takes(self, board): 
        self.directions = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1)]
        self.valid_moves = []
        for vertical_move, horizontal_move in self.directions:
            new_position = self.position.get_directional(vertical_move, horizontal_move)
            if new_position and board.get_piece_at_pos(new_position):
                self.valid_moves.append(new_position)
            
        return self.valid_moves

class Bishop(Piece):
    pass

class King(Piece):
    def get_valid_moves(self): 
        self.directions = [(i, j) for i in [1, 0, -1] for j in [1, 0, -1] if (i, j) != (0, 0)]
        self.valid_moves = []
        for vertical_move, horiontal_move in self.directions:
            new_position = self.position.get_directional(vertical_move, horiontal_move)
            self.valid_moves.append(new_position)
        return self.valid_moves

class Queen(Piece):
    pass

class Rook(Piece):
    pass