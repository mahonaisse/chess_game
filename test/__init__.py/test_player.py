from pieces import *
from board import *
import copy

def test_movePiece_stalemate()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    king = player1.findPieceByPieceName("K")
    len(player1.pieces) == 1 
    len(player2.pieces) == 1
    assert king.movePiece(3, 5, player1, player2) == "Stalemate"
    
def test_movePiece_checkmate()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop1 = player1.findPieceByPieceName("B1")
    player1.movePiece("P4", 4, 4, player2)
    opponent, checkingPiece
    assert king.movePiece(3, 5, player1, player2) == "checkmate"
    
def test_movePiece_checked()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop1 = player1.findPieceByPieceName("B1")
    player1.movePiece("P4", 4, 4, player2)
    assert bishop1.isValidMove(3, 5, player1, player2) == "checked"
    
def test_invalidmovePiece()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    assert player1.movePiece("P4", 4, 4, player2) == False
    


#true, false, checked, checkmate