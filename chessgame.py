import os

class ChessGame:
    def __init__(self, whitePlayer, blackPlayer):
        self.white = whitePlayer
        self.black = blackPlayer
        self.board = Board()
        
    def show_menu(self):
        os.system('clear')
        typeGame = None
        inMenu = True
        menu= """             
              chess: the game

                     _:_
                    '-.-'
                   __.'.__
  [O] 1 player    |_______|
                   \=====/
  [T] 2 players     )___(
                   /_____\\
  [L] load game     |   |
                    |   |
  [H] how to play   |   |
                    |   |
  [Q] quit          |   |
                   /_____\\
                  (=======)
                  }======={
                 (_________)
"""
        print(menu)
    
        while True:
            try:
                typeGame = input("Enter 1 for New Game, 2 for Load Game, or 3 for Play Custom Games: ")
                if typeGame != 0:
                    if typeGame == '1':
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
    
#    def chess_variant():
#        pass

    def display_game(self):
        os.system('clear')
        whiteTurn = """
                White to move
        """
        
        blackTurn = """
               Black to move
        """

        gameChoices = """
[M] move a piece   [U] undo a move  [R] randomize move
[C] cancel action  [E] main menu    [Q] quit
        """

        print(whiteTurn)

        rowNumber = 8
        while rowNumber > 0:
            print("        ", rowNumber, "  ┃ ", end = "")
            
            # iterate through teams somehow
            # the dots displayed on the lines are an example
            for i in range(8):
                print("• ", end = "")

            print("")
            rowNumber = rowNumber - 1
        print("             ┗━━━━━━━━━━━━━━━━━")
        print("               a b c d e f g h")

        print(gameChoices)
        action = input("[ ] please input an action: ")




class Player:
    pass

class Board:
    def __init__(self):
        pass

