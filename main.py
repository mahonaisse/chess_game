from player import Player
from board import displayBoard
import os
#from pieces import Position, Pieces
#from menu import

os.system('clear')

white_players_name = input("Enter white player's name: ")
white_player = Player(white_players_name, 'W')

black_players_name = input("Enter black player's name: ")
black_player = Player(black_players_name, 'B')

# os.system('clear')

displayBoard(white_player, black_player)

move = 'Default_Move'
non_current_player_checkmated = False

current_players_name = white_players_name
non_current_players_name = black_players_name

current_player = white_player
non_current_player = black_player

# get initial move
while not non_current_player_checkmated:
    print(f"It is {current_players_name}'s turn. ")
    name_of_piece_to_move = input(f'What piece do you want to move, {current_players_name}? ')
    piece_to_move = current_player.findPieceByPieceName(name_of_piece_to_move)
    while not piece_to_move:
        name_of_piece_to_move = input('Invalid piece. Please input valid piece name: ')
        piece_to_move = current_player.findPieceByPieceName(name_of_piece_to_move)

    target_rank = int(input('Enter target rank: '))
    while target_rank < 1 or target_rank > 8:
        target_rank = int(input('Target rank is invalid. Please enter a valid rank: '))

    target_file = int(input('Enter target file: '))
    while target_file < 1 or target_file > 8:
        target_file = int(input('Target file is invalid. Please enter a valid file: '))

    # os.system('clear')
    move = current_player.movePiece(name_of_piece_to_move, target_rank, target_file, non_current_player)        

    if move: # if move is valid

        # check if either player is checkmated
        print(piece_to_move)
        non_current_player_checkmated = non_current_player.isCheckMate(current_player, piece_to_move)
        print(f'Is {non_current_players_name} is checkmated? {non_current_player_checkmated}')

        # swap current player and current player's name
        current_player, non_current_player = non_current_player, current_player
        current_players_name, non_current_players_name = non_current_players_name, current_players_name


    else: # move is invalid
        print('Invalid move. Please try again.')







# while not white_player_checkmated and not black_player_checkmated:
#     name_of_piece_to_move = input(f'What piece do you want to move, {black_players_name}? ')
#     piece_to_move = black_player.findPieceByPieceName(name_of_piece_to_move)
    
#     while not piece_to_move:
#         name_of_piece_to_move = input('Invalid piece. Please input valid piece name: ')
#         piece_to_move = black_player.findPieceByPieceName(name_of_piece_to_move)

#     target_rank = int(input('Enter target rank: '))
#     while target_rank < 1 or target_rank > 8:
#         target_rank = int(input('Target rank is invalid. Please enter a valid rank: '))

#     target_file = int(input('Enter target file: '))
#     while target_file < 1 or target_file > 8:
#         target_file = int(input('Target file is invalid. Please enter a valid file: '))

#     white_player_checkmated = white_player.isCheckMate(black_player, white_player.findPieceByPieceName(piece_to_move))
#     black_player_checkmated = black_player.isCheckMate(white_player, black_player.findPieceByPieceName(piece_to_move))
        
    
