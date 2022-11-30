from pieces import *
from board import *
import copy

# def test_movePiece_stalemate()-> None:
#     player1 = Player("Charles", "W")
#     player2 = Player("Harry", "B")
    
#     king = player1.findPieceByPieceName("K")
#     len(player1.pieces) == 1 
#     len(player2.pieces) == 1
#     player1.remove("p1", 2, 1)
#     player1.remove("p2", 2, 1)

#     assert king.movePiece(3, 5, player1, player2) == "Stalemate"

# Test Scenario 1 Fools Mate
def test_movePiece_checked()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    player1.movePiece("P2" , 4, 2, player2)
    player2.movePiece("p4", 5, 4, player1)
    player1.movePiece("P3" , 4, 3, player2)
    assert player2.movePiece("q", 4, 1, player1) == "checked"
    
# def test_movePiece_checked()-> None:
#     player1 = Player("Charles", "W")
#     player2 = Player("Harry", "B")
    
#     bishop1 = player1.findPieceByPieceName("B1")
#     player1.movePiece("P4", 4, 4, player2)
#     assert bishop1.isValidMove(3, 5, player1, player2) == "checked"
    
def test_invalidmovePiece()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    player1.movePiece("P4", 4, 4, player2)
    player2.movePiece("p4", 5, 4, player1)
    player1.movePiece("B1", 4, 6, player2)
    player2.movePiece("n2", 6, 6, player1)
    player1.movePiece("Q", 5, 1, player2)
    player2.movePiece("n1", 6, 3, player1)
    player1.movePiece("Q", 7, 3, player2)    
    assert player2.movePiece("k", 7, 7, player1) == False
    
