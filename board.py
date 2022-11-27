from player import *
from pieces import *

def updateBoard(player1, player2):
    board = [[None for i in range(0,9)] for j in range(0, 9)]
    for p in player1.pieces:
        board[p.pRank][p.pFile] = p 
    for p in player2.pieces:
        board[p.pRank][p.pFile] = p 
    return board

def displayBoard(player1, player2):
    CGREEN = '\033[32m'
    CEND = '\033[0m'
    board = updateBoard(player1, player2)
    #White on Bottom Black on Top
    print('*'*35)
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

def displayBoardReverse(board):
    #White on Bottom Black on Top
    for row in range(8,0,-1):
        for col in range(8,0,-1):
            p = board[row][col]
            if(p != None):
                print(f'{board[row][col].name:<2}', end=" ")
            else:
                print(" "*2, end = " ")
        print()
