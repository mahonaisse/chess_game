from board import * 
from player import *
from pieces import *

# import unittest

def test_pawn_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    pawn2 = player1.findPieceByPieceName("p2")
    assert pawn2.isValidMove(4, 2, player1, player2) == True 
    
def test_pawn_isValidMove2()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    pawn1 = player1.findPieceByPieceName("p1")
    assert pawn1.isValidMove(4, 1, player1, player2) == True
    
def test_pawn_not_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    pawn2 = player1.findPieceByPieceName("p2")
    assert pawn2.isValidMove(4, 1, player1, player2) == False
    
def test_pawn_capture_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    pawn1 = player1.findPieceByPieceName("p1")
    pawn2 = player2.findPieceByPieceName("p2")
    player1.movePiece("P1", 4, 1, player2)  
    player2.movePiece("P2", 5, 2, player1)
    assert pawn1.isValidMove(5, 2, player1, player2) == "capture"
    
def test_knight_not_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    knight2 = player1.findPieceByPieceName("n2")
    assert knight2.isValidMove(8, 1, player1, player2) == False 
    
def test_knight_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    knight1 = player1.findPieceByPieceName("n1")
    assert knight1.isValidMove(3, 3, player1, player2) == True
    
def test_knight_isValidMove_capture()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    knight1 = player1.findPieceByPieceName("N1")
    player1.movePiece("N1", 3, 3, player2)
    player2.movePiece("p4" , 5, 4, player1)
    assert knight1.isValidMove(5, 4, player1, player2) == "capture"
    
def test_bishop_not_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop2 = player1.findPieceByPieceName("b2")
    assert bishop2.isValidMove(8, 1, player1, player2) == False 
    
def test_bishop_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    bishop1 = player1.findPieceByPieceName("B1")
    player1.movePiece("P4", 4, 4, player2)
    assert bishop1.isValidMove(3, 5, player1, player2) == True
    
# #case 2 for bishop; up and left
# def test_bishop_isValidMove_up_left()-> None:
#     player1 = Player("Charles", "W")
#     player2 = Player("Harry", "B")
    
#     bishop1 = player1.findPieceByPieceName("B1")
#     player1.movePiece("P4", 3, 5, player2)
#     assert bishop1.isValidMove(3, 5, player1, player2) == True

    
def test_king_not_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    king = player1.findPieceByPieceName("K")
    assert king.isValidMove(8, 1, player1, player2) == False 
    
def test_king_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    king = player1.findPieceByPieceName("K")
    assert king.isValidMove(8, 1, player1, player2) == False
    
    
def test_queen_not_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    queen = player1.findPieceByPieceName("Q")
    assert queen.isValidMove(8, 1, player1, player2) == False 
    
def test_queen_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    queen = player1.findPieceByPieceName("Q")
    player1.movePiece("P4", 4, 4, player2)
    assert queen.isValidMove(2, 4, player1, player2) == True
    
def test_rook_not_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    rook1 = player1.findPieceByPieceName("R1")
    assert rook1.isValidMove(8, 1, player1, player2) == False 
    
def test_rook_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    rook1 = player1.findPieceByPieceName("r1")
    player1.movePiece("P1", 4, 1, player2)
    assert rook1.isValidMove(3, 1, player1, player2) == True
    





