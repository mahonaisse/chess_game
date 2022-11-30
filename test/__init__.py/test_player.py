from pieces import *
from board import *
import copy

def test_movePiece_stalemate()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop1 = player1.findPieceByPieceName("B1")
    player1.movePiece("P4", 4, 4, player2)
    assert bishop1.isValidMove(3, 5, player1, player2) == "Stalemate"
    
def test_movePiece_()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop1 = player1.findPieceByPieceName("B1")
    player1.movePiece("P4", 4, 4, player2)
    assert bishop1.isValidMove(3, 5, player1, player2) == True

#true, false, checked, checkmate