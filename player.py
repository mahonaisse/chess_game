from pieces import *

class Player:
    name = ''
    color = ''
    pieces = []
    lostPieces = []
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.pieces = []
        #intialize white pieces
        if(color == "W"):
            pawnRank = 2
            for i in range(1,9):
                p = Pawn( f"P{i}", color, pawnRank, i)
                print(p)
                self.pieces.append(p)
            pieceRank = 1
            self.pieces.append(Rook("R1", color, pieceRank, 1))
            self.pieces.append(Rook("R2", color, pieceRank, 8))
            self.pieces.append(Knight("N1", color, pieceRank, 2))
            self.pieces.append(Knight("N2", color, pieceRank, 7))
            self.pieces.append(Bishop("B1", color, pieceRank, 3))
            self.pieces.append(Bishop("B2", color, pieceRank, 6))
            self.pieces.append(King("K", color, pieceRank, 4))
            self.pieces.append(Queen("Q", color, pieceRank, 5))
        #initialize black pieces
        else:
            pawnRank = 7
            for i in range(1,9):
                p = Pawn( f"p{i}", color, pawnRank, i)
                self.pieces.append(p)
            rank = 8
            self.pieces.append(Rook("r1", color, rank, 1))
            self.pieces.append(Rook("r2", color, rank, 8))
            self.pieces.append(Knight("n1", color, rank, 2))
            self.pieces.append(Knight("n2", color, rank, 7))
            self.pieces.append(Bishop("b1", color, rank, 3))
            self.pieces.append(Bishop("b2", color, rank, 6))
            self.pieces.append(King("k", color, rank, 4))
            self.pieces.append(Queen("q", color, rank, 5))
    
        
    # def sPiecetoMove(pieceName, toRank, toFile):
    #     if piece in pieces:
    #         if piece.isValidMove(toRank, toFile):
    #             index = pieces.index(piece)
    #             pieces[index].pRank = toRank
    #             pieces[index].pFile = toFile
    #             return True
    #         else:
    #             print("Not Valid Move")
    #             return False
    #     else:
    #         print("Not Valid Piece")    
    #         return False
    def findPieceByPieceName(self, pieceName):
        for i in self.pieces:
            if i.name == pieceName:
                return i
        return None

    def findPieceByRankFile(self, atRank, atFile):
        for i in self.pieces:
            if i.pRank == atRank and i.pFile == atFile:
                return i
        return None
    
    def movePiece(self, pieceName, toRank, toFile, board):
        #Find the piece that based off the pieceName
        p = self.findPieceByPieceName(pieceName)
        if (p.isValidMove(toRank, toFile, board) == True):  
            p.pRank = toRank
            p.pFile = toFile
            return True
        elif(p.isValidMove(toRank, toFile, board) == "capture"):
            p.pRank = toRank
            p.pFile = toFile
            return "capture"
        else:
            print("invalid move")
            return False

    # def removePiece(self, pieceName):
    #     p = self.findPiece(pieceName)
    #     self.pieces.remove(p)
    def removePiece(self, atRank, atFile):
        p = self.findPieceByRankFile(atRank, atFile)
        self.pieces.remove(p)

    def __str__(self):
        return(f'name: {self.name} color: {self.color} \n {self.pieces}')

def updateBoard(player1, player2):
    board = [[None for i in range(0,9)] for j in range(0, 9)]
    for p in player1.pieces:
        board[p.pRank][p.pFile] = p 
    for p in player2.pieces:
        board[p.pRank][p.pFile] = p 
    return board

def displayBoard(board):
    
    #White on Bottom Black on Top

    print("*"*25)
    for row in range(1,9,1):
        for col in range(1,9,1):
            p = board[row][col]
            if(p != None):
                print(f'{board[row][col].name:<2}', end=" ")
            else:
                print(" "*2, end = " ")
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

#testing
player1 = Player("Charles", "W")
player2 = Player("Harry", "B")
print(player1)
print(player2)
board = updateBoard(player1, player2)
player1.movePiece("P1" , 4, 1, board)
board = updateBoard(player1, player2)
displayBoard(board)
displayBoardReverse(board)
player1.movePiece("R1" , 3, 1, board)
board = updateBoard(player1, player2)
displayBoard(board)
displayBoardReverse(board)
player1.movePiece("R1" , 3, 3, board)
board = updateBoard(player1, player2)
displayBoardReverse(board)
s = player1.movePiece("R1" , 7, 3, board)
if(s == "capture"):
    player2.removePiece(7,3)
board = updateBoard(player1, player2)
displayBoard(board)

s = player1.movePiece("N1" , 3, 3, board)
if(s == "capture"):
    player2.removePiece(3,3)
board = updateBoard(player1, player2)
displayBoard(board)

s = player2.movePiece("n1" , 6, 1, board)
if(s == "capture"):
    player1.removePiece(6,1)
board = updateBoard(player1, player2)
displayBoard(board)

s = player1.movePiece("P2" , 3, 2, board)
if(s == "capture"):
    print(f'{s} {board[7][3].name}')
    player1.removePiece(7,3)
board = updateBoard(player1, player2)
displayBoard(board)

s = player1.movePiece("B1" , 2, 2, board)
if(s == "capture"):
    print(f'{s} {board[7][3].name}')
    player1.removePiece(7,3)
board = updateBoard(player1, player2)
displayBoard(board)
s = player1.movePiece("B1" , 3, 1, board)
if(s == "capture"):
    print(f'{s} {board[7][3].name}')
    player1.removePiece(7,3)
board = updateBoard(player1, player2)
displayBoard(board)
s = player1.movePiece("B1" , 7, 5, board)
if(s == "capture"):
    print(f'{s} {board[7][5].name}')
    player2.removePiece(7,5)
board = updateBoard(player1, player2)
displayBoard(board)
# board = updateBoard(player1, player2)
# player1.movePiece("R1", 3, 1, board)


# player1.movePiece("P1" , 4, 1, board)
# board = updateBoard(player1, player2)
# print("\n\n\nAfter move")
# print(player1)
# player2.movePiece("p1" , 5, 1, board)
# board = updateBoard(player1, player2)
# print("\n\n\nAfter move")
# print(player2)
# displayBoard(board)
#print(board)
