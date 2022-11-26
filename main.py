from chessgame import ChessGame, Player, Board

game = ChessGame('white', 'black')
inMenu = True
inGame = True

while inMenu or inGame:
    #game.main_menu()
    
#    game.display_game('White')
   
    game.load_saved_game("all_pawns_saved_game.txt")
   
    break
        
