class ChessGame:
    def __init__(self, whitePlayer, blackPlayer):
        self.white = whitePlayer
        self.black = blackPlayer
        self.board = Board()
        
    def show_menu(self):
        typeGame = None
        menu= """             
              chess: the game

                     _:_
                    '-.-'
                   __.'.__
  [O] 1 player    |_______|
                   \=====/
  [T] 2 players     )___(
                   /_____\
  [L] load game     |   |
                    |   |
  [H] how to play   |   |
                    |   |
  [Q] quit          |   |
                   /_____\
                  (=======)
                  }======={
                 (_________)")
"""
        print(menu)
    
        while True:
            try:
                typeGame = int(input("Enter 1 for New Game, 2 for Load Game, or 3 for Play Custom Games")) 
                if typeGame=='1':
                    print("New Game entered successfully")
                    self.start_new_game()
                    break
                elif typeGame=='2':
                    print("Load Game entered successfully")
                    self.load_saved_game()
                    break
                elif typeGame=='3':
                    print("Play Custom Games entered successfully")
                    self.chess_variant()
                    break
                else:
                    print("Enter 1, 2 or 3")      
            except ValueError:
                print("Provide an integer value...")
                continue
            
    def start_new_game():
        #reset pieces to initial position
        pass
        
    def load_saved_game():
        pass
    
    def chess_variant():
        pass

class Player:
    pass

class Board:
    def __init__(self):
        pass

