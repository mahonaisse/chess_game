from pieces import *
from board import *
import copy

#FIXME
def test_isCheckMate_True()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop1 = player1.findPieceByPieceName("B1")
    player1.movePiece("P4", 4, 4, player2)
    assert bishop1.isValidMove(3, 5, player1, player2) == True
    
def test_isCheckMate_False()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop1 = player1.findPieceByPieceName("B1")
    player1.movePiece("P4", 4, 4, player2)
    assert bishop1.isValidMove(3, 5, player1, player2) == True

