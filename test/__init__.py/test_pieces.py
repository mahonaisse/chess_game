from board import * 
from player import *
from pieces import *

# import unittest

def test_pawn_not_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    # board = buildBoard(player1,player2)
    pawn2 = player1.findPieceByPieceName("p2")
    assert pawn2.isValidMove(4, 2, player1, player2) == False 
    #if not valid, expect capture, checkmate return check,
    
def test_pawn_isValidMove()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    # board = buildBoard(player1,player2)
    pawn1 = player1.findPieceByPieceName("p1")
    assert pawn1.isValidMove(4, 1, player1, player2) == True
    
def test_pawn_isValidMove_capture()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    # board = buildBoard(player1,player2)
    pawn2 = player1.findPieceByPieceName("p2")
    assert pawn2.isValidMove(4, 1, player1, player2) == "capture" 
    
#test other pieces- Knight, rook, queen
    
# player2.movePiece("p4", 5, 4, player1)
# player1.movePiece("P3" , 4, 3, player2)
# player2.movePiece("q", 4, 1, player1)



