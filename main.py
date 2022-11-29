from player import Player
from board import displayBoard
#from pieces import Position, Pieces
#from menu import

white_players_name = input("Enter white player's name: ")
white_player = Player(white_players_name, 'W')

black_players_name = input("Enter black player's name: ")
black_player = Player(black_players_name, 'B')

displayBoard(white_player, black_player)

move = None
white_player_checkmated = black_player_checkmated = False

current_players_name = white_players_name
non_current_players_name = black_players_name

current_player = white_player
non_current_player = black_player

# get initial move
while (not white_player_checkmated and not black_player_checkmated) or not move:
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


    move = current_player.movePiece(name_of_piece_to_move, target_rank, target_file, non_current_player)
    if not move:
        print('Invalid move. Please try again.')

    # swap current player and current player's name
    if move:
        current_player, non_current_player = non_current_player, current_player
        current_players_name, non_current_players_name = non_current_players_name, current_players_name


white_player_checkmated = white_player.isCheckMate(black_player, white_player.findPieceByPieceName(piece_to_move))
black_player_checkmated = black_player.isCheckMate(white_player, black_player.findPieceByPieceName(piece_to_move))








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
        
    
