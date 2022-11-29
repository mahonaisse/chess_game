from pieces import *
from board import *
import copy #use deepcopy() from copy module to deep copy a list

class Player:
    name = ''
    #color can only be "W" or "B" case sensitive
    color = ''
    pieces = []
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.pieces = []
        #intialize white pieces name for white piece will be uppercase can potentially change to lower case
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
        #initialize black pieces name for black piece will be lower case
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
    #this finds the piece object that has the same pieceName
    def findPieceByPieceName(self, pieceName):
        for i in self.pieces:
            if i.name.lower() == pieceName.lower():
                return i
        return None
    #this finds the piece object that is atRank and atFile
    def findPieceByRankFile(self, atRank, atFile):
        for i in self.pieces:
            if i.pRank == atRank and i.pFile == atFile:
                return i
        return None
    #TODO castle
    # def castle(self, opponent):
    #     king = k.findPieceByPieceName("k")
    #     kingRook = k.findPieceByPieceName("r1")
    #     queenRook = k.findPieceByPieceName("r2")
    #     if():
    #         return False
    #     else:
    #         if(kingRook.pRank == 1 and kingRook.pRank == 1):
    #             step = 1
    #             # 3 cause thats the difference between the King and 
    #             for i in range(1,3):
    #  promotes Pawn piece to Rook, Knight, Bishop or Queen if its at the right rank
    def promote(self, pawn, promoteTo):
        if(not (pawn.pRank == 8 or pawn.pRank == 1)):
            return "can not promote"
        else:
            countExisting = 0
            for p in self.pieces:
                if p.name[0].upper() == promoteTo.upper():
                    countExisting += 1
            name = f'{promoteTo}{countExisting}'
            if(promoteTo.upper() == "N"):
                pawn = Knight(name, self.color, pawn.pRank, pawn.pFile)
            if(promoteTo.upper() == "B"):
                pawn = Bishop(name, self.color, pawn.pRank, pawn.pFile)
            if(promoteTo.upper() == "R"):
                pawn = Rook(name, self.color, pawn.pRank, pawn.pFile)
            if(promoteTo.upper() == "Q"):
                pawn = Queen(name, self.color, pawn.pRank, pawn.pFile)
            
            return "promoted"
    
    #move the piece of pieceName to toRank and toFile
    def movePiece(self, pieceName, toRank, toFile, opponent):
        if(self.isStaleMate(opponent)):
            return "Stalemate"

        print(f'Move: {pieceName} Rank: {toRank} File: {toFile}')
        #Find the piece that based off the pieceName        
        p = self.findPieceByPieceName(pieceName)
        #move
        validMoveReturn = p.isValidMove(toRank, toFile, self, opponent)
        if (validMoveReturn != False): 
            #update piece position 
            self.updatePiece(p , toRank, toFile)
            result = validMoveReturn
            if(validMoveReturn == "capture"):                
                opponent.removePiece(toRank, toFile)
            #check if pawn can be promoted
            if(isinstance(p, Pawn)):
                queenName = "q" if p.color == "B" else "Q"
                self.promote(p, queenName)
            if(self.isCheck(p,opponent)):
                if(self.isCheckMate(opponent,p)):
                    print("checkmate!")
                    result = "checkmate"
                else:
                    print("checked!")
                    result = "checked"
            displayBoard(self, opponent)
            return result
        else:
            return False

    #remove piece atRank and atFile
    def removePiece(self, atRank, atFile):
        p = self.findPieceByRankFile(atRank, atFile)
        self.pieces.remove(p)
    
    #update piece rank and file to atRank and atFile
    def updatePiece(self, piece, atRank, atFile):
        piece.pRank = atRank
        piece.pFile = atFile
        
    #check if the piece is checking the opponenet
    def isCheck(self, piece, opponent):
        oppKing = opponent.findPieceByPieceName("k")
        #if the move to king position is valid it will be a check because you can "capture" the king
        return piece.isValidMove(oppKing.pRank, oppKing.pFile, self, opponent)
    
    #check if the player checkmated the opponent via checkingPiece
    def isCheckMate(self, opponent, checkingPiece):
        #if the king can't get of check and can't block and can't run it is check mate
        #DeMorgan's Law
        return not (self.canGetOutOfCheckByKingMove(opponent) or
            self.canGetOutOfCheckByBlock(opponent, checkingPiece) or
            self.canGetOutOfCheckByCapture(opponent, checkingPiece))
    #check if player and opponent are in stalemate state
    def isStaleMate(self, opponent):
        if(len(self.pieces) == 1 and len(opponent.pieces) == 1):
            return True
        #TODO add other conditions
        else:
            return False

    # King in Check
    # Check if any of the oppoents piece(not the king) can capture the piece that is checking the opponents king
    def canGetOutOfCheckByCapture(self, opponent, checkingPiece):
        for piece in opponent.pieces:
            if piece.name.upper() != "K":
                if piece.isValidMove(checkingPiece.pRank, checkingPiece.pFile, opponent, self) == "capture":
                    return True
        return False

    # king is in check
    # check if there is any valid moves for the king 
    # either by capture the piece checking it or run to a safe pos with no checks
    def canGetOutOfCheckByKingMove(self, opponent):
        oppKing = opponent.findPieceByPieceName("k")
        #case 1 go up
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile
        if(isOnBoard(toRank)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False
        #case 2 go up and right
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile + 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False

        #case 3 go right
        toRank = oppKing.pRank
        toFile = oppKing.pFile + 1
        if(isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False

        #case 4 go down and right
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile + 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False

        #case 5 go down
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile
        if(isOnBoard(toRank)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False
                
        #case 6 go down and left
        toRank = oppKing.pRank - 1
        toFile = oppKing.pFile - 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False

        #case 7 go left
        toRank = oppKing.pRank
        toFile = oppKing.pFile - 1
        if(isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False
            
        #case 8 go up and left
        toRank = oppKing.pRank + 1
        toFile = oppKing.pFile - 1
        if(isOnBoard(toRank) and isOnBoard(toFile)):
            if oppKing.isValidMove(toRank, toFile, opponent, self):
                return opponent.potentialNextMove(self, toRank, toFile)
            else:
                return False
        #all cases fail
        return False
    
    #check if there any piece move that can get inbetween the checking piece and the king
    def canGetOutOfCheckByBlock(self, opponent, checkingPiece):
        oppKing = opponent.findPieceByPieceName("k")
        rankDifference = abs(oppKing.pRank - checkingPiece.pRank)
        fileDifference = abs(oppKing.pFile - checkingPiece.pFile)
        #right in front of the king no way to block or is a knight move
        #can not be blocked
        if(fileDifference == 1 or rankDifference == 1):
            return False
        # same diagonal need to block along the diagonal
        if(rankDifference == fileDifference):
            fileStep = 1 if  checkingPiece.pFile > oppKing.pFile else -1
            rankStep = 1 if checkingPiece.pRank > oppKing.pRank else -1
            #find how many spaces one should check
            for i in range(1, rankDifference):   
                #step takes care which diagonal it goes             
                blockRank = oppKing.pRank + i*rankStep
                blockFile = oppKing.pFile + i*fileStep
                for piece in opponent.pieces:
                    if piece.name.upper() != "K":
                        if piece.isValidMove(blockRank, blockFile, opponent, self) == True:
                            # print(f"{piece.name} can block at {blockRank} {blockFile}")
                            return True
            return False
                    
        # same horizontal axis
        if(rankDifference == 0):
            fileStep = 1 if  checkingPiece.pFile > oppKing.pFile else -1
            for i in range(1, fileDifference):  
                blockFile = oppKing.pFile + i*fileStep
                blockRank = oppKing.pRank
                for piece in opponent.pieces:
                    if piece.name.upper() != "K":
                        if piece.isValidMove(blockRank, blockFile, opponent, self) == True:
                            return True

        #same vertical axis
        if(fileDifference == 0):
            rankStep = 1 if checkingPiece.pRank > oppKing.pRank else -1
            for i in range(1, fileDifference):  
                blockFile = oppKing.pFile
                blockRank = oppKing.pRank +  + i*rankStep
                for piece in opponent.pieces:
                    if piece.name.upper() != "K":
                        if piece.isValidMove(blockRank, blockFile, opponent, self) == True:
                            return True
        else:
            return False

    # check if any piece in the player's piece can move to the position 
    # that the opponent king is on oppKingRank, oppKingFile
    def canAnyPieceCaptureKing(self, opponent, oppKingRank, oppKingFile):
        for p in self.pieces:
            if p.name.upper() != "K":
                if p.isValidMove(oppKingRank, oppKingFile, self, opponent):
                    return True
        return False
    
    # check if a king's potential next move will cause itself to be in check
    def potentialNextMove(self, opponent, kingToRank, kingToFile):
        tempPlayer = copy.deepcopy(self)
        tempOpponent = copy.deepcopy(opponent)
        tempOpponent.removePiece(kingToRank, kingToFile)
        king = tempPlayer.findPieceByPieceName('k')
        tempPlayer.updatePiece(king, kingToRank, kingToFile)
        #if can capture means that the king can't walk there
        if tempOpponent.canAnyPieceCaptureKing(tempPlayer, kingToRank, kingToFile):
            return False
        else:
            return True
    
    def __str__(self):
        return(f'name: {self.name} color: {self.color} \n {self.pieces}')