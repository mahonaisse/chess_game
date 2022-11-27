class Position:
    def __init__(self, pos):
        self.FILE_TO_NUM = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        self.NUM_TO_FILE = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        self.VALID_POSITIONS = {
            'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
        }

        self.rank = int(pos[1])
        self.file = self.FILE_TO_NUM[pos[0]]

    def output_pos(self, file, rank):
        return f'{self.NUM_TO_FILE[file]}{rank}'

    def __str__(self):
        return self.output_pos(self.file, self.rank)

    def get_directional(self, vertical_movement, horizontal_movement):
        self.temp_rank = self.rank + vertical_movement
        self.temp_file = self.rank + horizontal_movement
        if 0 < self.temp_rank < 9 and 0 < self.temp_file < 9:
            return self.output_pos(self.temp_file, self.temp_rank)
        else:
            return None

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
    
    def isValidMove(self, moveToRank, moveToFile, board):
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
    


        # self.position = Position(piece_pos)
        # self.color = color
        # self.VALID_POSITIONS = {
        #     'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
        #     'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
        #     'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
        #     'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
        #     'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
        #     'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
        #     'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
        #     'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
        # }

    # def set_position(self, new_pos):
    #     self.position = Position(new_pos)

class Pawn(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, board):
        
        if(self.color == "W"):
            #capture rules
            if(moveToRank == self.pRank + 1 
            and (moveToFile == self.pFile -1 or moveToFile == self.pFile+1)):
                if(board[moveToRank][moveToFile].color == self.color):
                    return False
                if(board[moveToRank][moveToFile].color != self.color):
                    return True
                else:
                    return False
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
                #capture rules
            elif(moveToRank == self.pRank + 1 
            and (moveToFile == self.pFile -1 or moveToFile == self.pFile+1)):
                if(board[moveToRank][moveToFile].color == self.color):
                    return False
                if(board[moveToRank][moveToFile].color != self.color):
                    return True
                else:
                    return False
        else:
            #capture rules
            if(moveToRank == self.pRank - 1 
            and (moveToFile == self.pFile -1 or moveToFile == self.pFile+1)):
                if(board[moveToRank][moveToFile] != None):
                    return "capture"
                else:
                    return False
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
                #capture rules
            
        



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

    def isValidMove(self, moveToRank, moveToFile, board):
        rankDifference = abs(moveToRank - self.pRank)
        fileDifference = abs(moveToFile - self.pFile)
        #if a knight moves left/right 2 and up/down 1 or left/right 1 and up/down 2(L-Shape)
        if((rankDifference == 2 and fileDifference == 1)
            or (rankDifference == 1 and fileDifference == 2)):
            return self.canMoveOrCapture(moveToRank, moveToFile, board)
        else:
            return False

class Bishop(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, board):
        rankDifference = abs(moveToRank - self.pRank)
        fileDifference = abs(moveToFile - self.pFile)
        #if the differences aren't the same they aren't on a diagonal
        if(rankDifference != fileDifference):
            return False
        else:
            fileStep = 1 if moveToFile > self.pFile else -1
            rankStep = 1 if moveToRank > self.pRank else -1
            for i in range(1, rankDifference):   
                #step takes care which diagonal it goes             
                if board[self.pRank + i*rankStep][self.pFile + i*fileStep] != None:
                    return False
            #nothing in between
            return self.canMoveOrCapture(moveToRank, moveToFile, board)

class King(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, board):
        rankDifference = abs(self.pRank - moveToRank)
        fileDifference = abs(self.pFile - moveToFile)
        if(rankDifference == 1 or fileDifference == 1):
            return self.canMoveOrCapture(moveToRank, moveToFile, board)
        else:
            return False

class Queen(Piece):
    def __init__(self, name, color, pRank, pFile):
        super().__init__(name, color, pRank, pFile)

    def isValidMove(self, moveToRank, moveToFile, board):
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
            elif(moveToFile == self.pFile):
                # print("Same File")

                step = 1 if moveToRank > self.pRank else -1
                print(step)
                for i in range(1, rankDifference):
                    #Invalid: when something along the way
                    if(board[self.pRank + i*step][moveToFile] != None):
                        return False
                #Nothing in the way
                # print("Nothing in the way")
                return self.canMoveOrCapture(moveToRank, moveToFile, board)
            else:
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
    
    def isValidMove(self, moveToRank, moveToFile, board):
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
                print(step)
                for i in range(1, rankDifference):
                    #Invalid: when something along the way
                    if(board[ self.pRank +i * step][moveToFile] != None):
                        return False
                #Nothing in the way
                # print("Nothing in the way")
                return self.canMoveOrCapture(moveToRank, moveToFile, board)