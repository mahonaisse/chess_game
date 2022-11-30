from board import * 
from player import *
from pieces import *

def test_buildBoard_default()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    board=buildBoard(player1,player2)
    assert True
    
def test_displayBoard_default()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    board=buildBoard(player1,player2)
    assert True
 
def test_displayBoardReverse_default()-> None:
    player1 = Player("Charles", "W")
    player2 = Player("Harry", "B")
    board=buildBoard(player1,player2)
    assert True

