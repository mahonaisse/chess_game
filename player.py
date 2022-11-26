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
        #intialize pawn pieces
        if(color == "W"):
            rank = 2
        else:
            rank = 7
        for i in range(1,9):
            p = Pawn( f"P{i}", color, rank, i)
            self.pieces.append(p)
        #initialize other pieces
        if(color == "W"):
            rank = 1
        else:
            rank = 8
        self.pieces.append(Rook("R1", color, rank, 1))
        self.pieces.append(Rook("R2", color, rank, 8))
        self.pieces.append(Knight("N1", color, rank, 2))
        self.pieces.append(Knight("N2", color, rank, 7))
        self.pieces.append(Bishop("B1", color, rank, 3))
        self.pieces.append(Bishop("B2", color, rank, 6))
        if(color == "W"):
            self.pieces.append(King("K", color, rank, 4))
            self.pieces.append(Queen("Q", color, rank, 5))
        else:
            self.pieces.append(King("K", color, rank, 5))
            self.pieces.append(Queen("Q", color, rank, 4))
    
        
    def selectPiecetoMove(piece, toRank, toFile):
        if piece in pieces:
            if piece.isValidMove(toRank, toFile):
                index = pieces.index(piece)
                pieces[index].pRank = toRank
                pieces[index].pFile = toFile
                return True
            else:
                print("Not Valid Move")
                return False
        else:
            print("Not Valid Piece")    
            return False
    def __repr__(self):
        return (f'name : {self.name} \ncolor : {self.color}')

P1 = Player("Charles", "W")
print(P1)