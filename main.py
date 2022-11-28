from chessgame import ChessGame, Player, Board
from pieces import Position, Piece, Pawn, Knight, King, Queen, Rook

if __name__ == '__main__':
    board = Board()
    player1 = Player()

    board.move_piece('b1', 'a3', player1)
    board.move_piece('a3', 'b5', player1)
    board.move_piece('b5', 'a7', player1)
