from chessgame import ChessGame, Player, Board

game = ChessGame('white', 'black')
inMenu = True
inGame = True

while inMenu or inGame:
    #game.main_menu()
    board = Board()
    game.display_game(board, 'Black')
    break
        
