from player import *
from board import *

class Piece:
    name = ''
    color = ''
    pRank = -1
    pFile = -1
    def __init__(self, name, color, pRank, pFile):
        self.name = name
        self.color = color 
        self.pRank = pRank
        self.pFile = pFile
    def __str__(self):
        return (f'name: {self.name} color: {self.color} rank: {self.pRank} file: {self.pFile}')
    def __repr__(self):
        return (f'Pieces(name: {self.name} color: {self.color} rank: {self.pRank} file: {self.pFile})')
    
    def isValidMove(self, moveToRank, moveToFile, player, opponent):
        pass
    def canMoveOrCapture(self, moveToRank, moveToFile, board):
        
        #Can move to the position 
        if(board[moveToRank][moveToFile] == None):
            return True
        #Own piece on the position
        elif(board[moveToRank][moveToFile].color == self.color):
            return False
        #Opposing piece on the position to capture
        else:
            return "capture"

class Pawn(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, player, opponent):
        board = updateBoard(player,opponent)
        if(self.color == "W"):
            #capture rules
            if(moveToRank == self.pRank + 1 
            and (moveToFile == self.pFile -1 or moveToFile == self.pFile+1)):
                #no piece
                if(board[moveToRank][moveToFile] == None):
                    return False
                #your piece
                elif(board[moveToRank][moveToFile].color == self.color):
                    return False
                #opponent piece
                elif(board[moveToRank][moveToFile].color != self.color):
                    return "capture"
            #see if any piece in front of it
            elif(board[self.pRank + 1][self.pFile] != None):
                return False
            #at rank 2 it can move 1 step or 2 step
            elif(self.pRank == 2 and board[self.pRank + 2][self.pFile] == None):
                if((moveToRank == 3 or moveToRank == 4) and moveToFile == self.pFile):
                    return True
                else:
                    return False
            #can move only one step at a time after rank 2
            elif(self.pRank > 2):
                if(moveToRank == self.pRank + 1  and moveToFile == self.pFile):
                    return True
                else:
                    return False
        else:
            #capture rules
            if(moveToRank == self.pRank - 1 
            and (moveToFile == self.pFile -1 or moveToFile == self.pFile+1)):
                if(board[moveToRank][moveToFile] == None):
                    return False
                #your piece
                elif(board[moveToRank][moveToFile].color == self.color):
                    return False
                #opponent piece
                elif(board[moveToRank][moveToFile].color != self.color):
                    return "capture"
                
            #see if any piece in front of it
            elif(board[self.pRank - 1][self.pFile] != None):
                return False
            #move 2 steps it at rank 7
            elif(self.pRank == 7 and board[self.pRank - 2][self.pFile] == None):
                if((moveToRank == 6 or moveToRank == 5) and moveToFile == self.pFile):
                    return True
                else:
                    return False
            #move only one step after rank 7
            elif(self.pRank < 7):
                if(moveToRank == self.pRank - 1 and moveToFile == self.pFile):
                    return True
                else:
                    return False
                
            
        



    # def get_valid_moves(self):
    #     self.directions = []
    #     if self.color == 'W': # white pawns can move forward
    #         self.directions.append((1, 0))
    #     elif self.color == 'B': # black pawns can move backward
    #         self.directions.append((-1, 0))

    #     # TODO: add more directions based on if there is a piece in that location the pawn can take. Pass the board as a parameter, maybe with a getter function to identify the piece at that position. 
    #     self.valid_moves = []
    #     for vertical_move, horizontal_move in self.directions:
    #         new_position = self.position.get_directional(vertical_move, horizontal_move)
    #         self.valid_moves.append(new_position)
        
    #     return self.valid_moves
    pass

class Knight(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, player, opponent):
        board = updateBoard(player,opponent)
        #first find the difference in rank and file
        rankDifference = abs(moveToRank - self.pRank)
        fileDifference = abs(moveToFile - self.pFile)
        #a knight moves left/right 2 and up/down 1 or left/right 1 and up/down 2(L-Shape)
        if((rankDifference == 2 and fileDifference == 1)
            or (rankDifference == 1 and fileDifference == 2)):
            return self.canMoveOrCapture(moveToRank, moveToFile, board)
        #not a knight move
        else:
            return False

class Bishop(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, player, opponent):
        board = updateBoard(player,opponent)
        #find difference in between rank and file
        rankDifference = abs(moveToRank - self.pRank)
        fileDifference = abs(moveToFile - self.pFile)
        #if the differences aren't the same they aren't on a diagonal
        if(rankDifference != fileDifference):
            return False
        else:
            #find which direction the file is moving in and which direction rank is moving in
            #4 possibilites
            fileStep = 1 if moveToFile > self.pFile else -1
            rankStep = 1 if moveToRank > self.pRank else -1
            #find how many spaces one should check does not check the final destination
            for i in range(1, rankDifference):   
                #step takes care which diagonal it goes             
                if board[self.pRank + i*rankStep][self.pFile + i*fileStep] != None:
                    return False
            #nothing in between
            #checks the final destination see if its own piece is on there or not
            return self.canMoveOrCapture(moveToRank, moveToFile, board)

class King(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)
    #TODO implement so king can't move into check
    def isValidMove(self, moveToRank, moveToFile, player, opponent):
        board = updateBoard(player,opponent)
        rankDifference = abs(self.pRank - moveToRank)
        fileDifference = abs(self.pFile - moveToFile)
        #rank difference and/or file differnce should be 1
        if(rankDifference == 1 or fileDifference == 1):

            #this step is to see if any of the opponents pieces can capture the king
            #going to move to
            if opponent.canAnyPieceCaptureKing(player, moveToRank, moveToFile):
                return False
            else:
                return self.canMoveOrCapture(moveToRank, moveToFile, board)
        else:
            return False

class Queen(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, player, opponent):
        # combine rook and bishop moves
        board = updateBoard(player,opponent)
        rankDifference = abs(moveToRank - self.pRank)
        fileDifference = abs(moveToFile - self.pFile)
        if(rankDifference == fileDifference or moveToRank != self.pRank or moveToFile != self.pRank):
            #move across file, move horizontally
            if(moveToRank == self.pRank):
                # print("Same Rank")
                step = 1 if moveToFile > self.pFile else -1
                for i in range(1, fileDifference):
                    #Invalid: when something along the way
                    if(board[moveToRank][self.pFile + i * step] != None):
                        return False
                #Nothing in the way
                return self.canMoveOrCapture(moveToRank, moveToFile, board)
            #move across rank, move vertically
            if(moveToFile == self.pFile):
                # print("Same File")

                step = 1 if moveToRank > self.pRank else -1
                for i in range(1, rankDifference):
                    #Invalid: when something along the way
                    if(board[self.pRank + i*step][moveToFile] != None):
                        return False
                #Nothing in the way
                # print("Nothing in the way")
                return self.canMoveOrCapture(moveToRank, moveToFile, board)
            if(rankDifference == fileDifference):
                fileStep = 1 if moveToFile > self.pFile else -1
                rankStep = 1 if moveToRank > self.pRank else -1
                for i in range(1, rankDifference):   
                    #step takes care which diagonal it goes             
                    if board[self.pRank + i*rankStep][self.pFile + i*fileStep] != None:
                        return False
            #nothing in between
                return self.canMoveOrCapture(moveToRank, moveToFile, board)
            else:
                return False
        
            
            
            

        

class Rook(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)
    
    def isValidMove(self, moveToRank, moveToFile, player, opponent):
        board = updateBoard(player,opponent)
        #Invalid move: when not in a straight line
        if(moveToRank != self.pRank and moveToFile != self.pRank):
            return False
        else:
            rankDifference = abs(moveToRank - self.pRank)
            fileDifference = abs(moveToFile - self.pFile)
            #move across file, move horizontally
            if(moveToRank == self.pRank):
                # print("Same Rank")
                step = 1 if moveToFile > self.pFile else -1
                for i in range(1, fileDifference):
                    #Invalid: when something along the way
                    if(board[moveToRank][self.pFile + i *step] != None):
                        return False
                #Nothing in the way
                return self.canMoveOrCapture(moveToRank, moveToFile, board)
            #move across rank, move vertically
            else:
                # print("Same File")
                step = 1 if moveToRank > self.pRank else -1
                for i in range(1, rankDifference):
                    #Invalid: when something along the way
                    if(board[ self.pRank +i * step][moveToFile] != None):
                        return False
                #Nothing in the way
                # print("Nothing in the way")
                return self.canMoveOrCapture(moveToRank, moveToFile, board)