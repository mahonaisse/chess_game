from pieces import *
from board import *

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
        validMoveReturn = p.isValidMove(toRank, toFile, self, opponent)
        if (validMoveReturn != False):  
            p.pRank = toRank
            p.pFile = toFile
            result = validMoveReturn
            if(validMoveReturn == "capture"):                
                opponent.removePiece(toRank, toFile)
            if(self.isCheck(p,opponent)):
                if(self.isCheckMate(opponent,p)):
                    print("checkmate!")
                    result = "checkmate"
                else:
                    print("checked!")
                    result = "checked"
            return result
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
        return piece.isValidMove(oppKing.pRank, oppKing.pFile, self, opponent)
    
    def isCheckMate(self, opponent, checkingPiece):
        return not (self.canGetOutOfCheckByKingMove(opponent) or
            self.canGetOutOfCheckByBlock(opponent, checkingPiece) or
            self.canGetOutOfCheckByCapture(opponent, checkingPiece))
    
    # King in Check
    # See if any of the oppoents piece can capture the piece that is checking the opponents king
    def canGetOutOfCheckByCapture(self, opponent, checkingPiece):
        for piece in opponent.pieces:
            # if piece.name.upper() != "K":
            if piece.isValidMove(checkingPiece.pRank, checkingPiece.pFile, opponent, self) == "capture":
                return True
        return False


    # king is in check
    # this function if there is any valid moves for the king 
    # either by capture the piece checking it or run to a safe pos with no checks
    def canGetOutOfCheckByKingMove(self, opponent):
        board = updateBoard(self, opponent)
        oppKingName = 'k' if opponent.color == "B" else "K"
        oppKing = opponent.findPieceByPieceName(oppKingName)
        
        #case 1 go up
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile
        if(isOnBoard(toRank)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True
                
        #case 2 go up and right
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile + 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True

        #case 3 go right
        toRank = oppKing.pRank
        toFile = oppKing.pFile + 1
        if(isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True

        #case 4 go down and right
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile + 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True

        #case 5 go down
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile
        if(isOnBoard(toRank)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True
                
        #case 6 go down and left
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile - 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True

        #case 7 go left
        toRank = oppKing.pRank
        toFile = oppKing.pFile - 1
        if(isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True
            
        #case 8 go up and left
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile - 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return True
        return False

    def canGetOutOfCheckByBlock(self, opponent, checkingPiece):
        return False

    # can any piece in the player's piece can move to the position 
    # that the opponent king can move to oppKingToRank, oppKingToFile
    def canAnyPieceCaptureKing(self, opponent, oppKingToRank, oppKingToFile):
        for p in self.pieces:
            if p.name.upper() != "K":
                if p.isValidMove(oppKingToRank, oppKingToFile, self, opponent):
                    return True
        return False

    def __str__(self):
        return(f'name: {self.name} color: {self.color} \n {self.pieces}')

