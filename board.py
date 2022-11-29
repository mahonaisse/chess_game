from player import *
from pieces import *
#not a board class 
#can be used to display board, update board, etc.

#builds a board based on players' pieces
def buildBoard(player1, player2):
    board = [[None for i in range(0,9)] for j in range(0, 9)]
    for p in player1.pieces:
        board[p.pRank][p.pFile] = p 
    for p in player2.pieces:
        board[p.pRank][p.pFile] = p 
    return board

# display board built on players' pieces
# white is white black is green
# white on bottom black on top(proper way)
def displayBoard(player1, player2):
    CGREEN = '\033[32m'
    CEND = '\033[0m'
    board = buildBoard(player1, player2)
    #White on Bottom Black on Top
    print('*'*35)
    print ('R/F A | B | C | D | E | F | G | H |')
    print ('R/F 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
    for row in range(8,0,-1):
        print(row, end="| ")
        for col in range(8,0,-1):
            p = board[row][col]
            if(p != None):
                if p.color == 'B':
                    print(CGREEN + f'{p.name:<2}' + CEND, end=' |')
                else:
                    print(f'{p.name:<2}', end=' |')                
            else:
                print(" "*2, end = " |")
        print()

# display board built on players' pieces
# white is white black is green
# white on top black on bottom
def displayBoardReverse(player1, player2):
    CGREEN = '\033[32m'
    CEND = '\033[0m'
    board = buildBoard(player1, player2)
    #White on Bottom Black on Top
    print('*'*35)
    print ('R/F A | B | C | D | E | F | G | H |')
    print ('R/F 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
    for row in range(1,9,1):
        print(row, end="| ")
        for col in range(1,9,1):
            p = board[row][col]
            if(p != None):
                if p.color == 'B':
                    print(CGREEN + f'{p.name:<2}' + CEND, end=' |')
                else:
                    print(f'{p.name:<2}', end=' |')                
            else:
                print(" "*2, end = " |")
        print()

def isOnBoard(index):
    return index >= 1 and index <= 8