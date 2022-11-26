class Player:
    name = ''
    color = ''
    pieces = []
    lostPieces = []
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.pieces = []
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