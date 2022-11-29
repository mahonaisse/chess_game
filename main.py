from player import Player
from board import displayBoard
#from pieces import Position, Pieces
#from menu import

white_players_name = input("Enter white player's name: ")
white_player = Player(white_players_name, 'W')

black_players_name = input("Enter black player's name: ")
black_player = Player(black_players_name, 'B')

displayBoard(white_player, black_player)

name_of_piece_to_move = input(f'What piece do you want to move, {white_players_name}? ')
piece_to_move = white_player.findPieceByPieceName(name_of_piece_to_move)
while not piece_to_move:
    name_of_piece_to_move = input('Invalid piece. Please input valid piece name: ')
    piece_to_move = white_player.findPieceByPieceName(name_of_piece_to_move)

# while not (player1.isCheckMate(player2, player1.findPieceByPieceName('Q')))
