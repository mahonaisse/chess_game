from pieces import *

def updateBoard(player1, player2):
    board = [[None for i in range(0,9)] for j in range(0, 9)]
    for p in player1.pieces:
        board[p.pRank][p.pFile] = p 
    for p in player2.pieces:
        board[p.pRank][p.pFile] = p 
    return board

def displayBoard(player1, player2):
    board = updateBoard(player1, player2)
    #White on Bottom Black on Top
    print('*'*35)
    print ('R/F 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
    for row in range(1,9,1):
        print(row, end="| ")
        for col in range(1,9,1):
            p = board[row][col]
            if(p != None):
                print(f'{board[row][col].name:<2}', end=" |")
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
    
    def movePiece(self, pieceName, toRank, toFile, opponent):
        board = updateBoard(self, opponent)
        #Find the piece that based off the pieceName
        p = self.findPieceByPieceName(pieceName)
        #move
        if (p.isValidMove(toRank, toFile, board) == True):  
            p.pRank = toRank
            p.pFile = toFile
            if(self.isCheck(p,opponent)):
                return "checked"
            else:
                return "moved"
        #move and capture
        elif(p.isValidMove(toRank, toFile, board) == "capture"):
            p.pRank = toRank
            p.pFile = toFile
            opponent.removePiece(toRank, toFile)
            if(self.isCheck(p,opponent)):
                return "checked"
            else:
                return "captured"
        else:
            return "invalid move"

    # def removePiece(self, pieceName):
    #     p = self.findPiece(pieceName)
    #     self.pieces.remove(p)
    def removePiece(self, atRank, atFile):
        p = self.findPieceByRankFile(atRank, atFile)
        self.pieces.remove(p)
    
    def isCheck(self, piece, opponent):
        board = updateBoard(self, opponent)
        oppKingName = 'k' if opponent.color == "B" else "K"
        oppKing = opponent.findPieceByPieceName(oppKingName)
        #if the move to king position is valid it will be a check because you can "capture" the king
        return piece.isValidMove(oppKing.pRank, oppKing.pFile, board)
    
    def isCheckMate(self, piece, opponent):
        return not (self.canGetOutOfCheckByRun(piece,opponent) or
            self.canGetOutOfCheckByBlock(piece, opponent) or
            self.canGetOutOfCheckByCapture(piece,opponent))

    def canGetOutOfCheckByCapture(self, piece, opponent):
        return True

    def canGetOutOfCheckByRun(self, piece, opponent):
        board = updateBoard(self, opponent)
        oppKingName = 'k' if opponent.color == "B" else "K"
        oppKing = opponent.findPieceByPieceName(oppKingName)
        
        #case 1 go up
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile
        if(isOnBoard(toRank)):
            if oppKing.isValidMove(toRank, toFile):
                return True
                
        #case 2 go up and right
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile + 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile):
                return True

        #case 3 go right
        toRank = oppKing.pRank
        toFile = oppKing.pFile + 1
        if(isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile):
                return True

        #case 4 go down and right
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile + 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile):
                return True

        #case 5 go down
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile
        if(isOnBoard(toRank)):
            if oppKing.isValidMove(toRank, toFile):
                return True
                
        #case 6 go down and left
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile - 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile):
                return True

        #case 7 go left
        toRank = oppKing.pRank
        toFile = oppKing.pFile - 1
        if(isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile):
                return True
            
        #case 8 go up and left
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile - 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile):
                return True
        
        return False
    def canGetOutOfCheckByBlock(self, piece, opponent):
        return True
    
    def isOnBoard(index):
        return index >= 1 and index <= 8

    def __str__(self):
        return(f'name: {self.name} color: {self.color} \n {self.pieces}')

