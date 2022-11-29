from board import * 
from player import *
from pieces import *
import unittest

def test_scenario1()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    
    # assert player1.movePiece("P2" , 4, 2, player2) == True
    #if not valid, expect capture, checkmate return check,
    
# player2.movePiece("p4", 5, 4, player1)
# player1.movePiece("P3" , 4, 3, player2)
# player2.movePiece("q", 4, 1, player1)