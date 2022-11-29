from player import *
from pieces import *


player1 = Player("Charles", "W")
player2 = Player("Harry", "B")
# player1.movePiece("P1", 4, 1, player2)
# player1.movePiece("R1" , 3, 1, player2)
# player1.movePiece("R1", 3, 3, player2)
# player1.movePiece("R1", 3, 1, player2)
# player1.movePiece("R1", 1, 1, player2)
# player1.movePiece("P4", 4, 4, player2)
player1.movePiece("P5", 4, 5, player2)
player1.movePiece("Q", 3, 5, player2)
player1.movePiece("Q", 3, 4, player2)
player1.movePiece("Q", 3, 5, player2)
player1.movePiece("Q", 1, 5, player2)



# Test Scenario 1 Fools Mate
# player1.movePiece("P2" , 4, 2, player2)
# player2.movePiece("p4", 5, 4, player1)
# player1.movePiece("P3" , 4, 3, player2)
# player2.movePiece("q", 4, 1, player1)


#Test Scenario 2 Scholars' mate
# player1.movePiece("P4", 4, 4, player2)
# player2.movePiece("p4", 5, 4, player1)
# player1.movePiece("B1", 4, 6, player2)
# player2.movePiece("n2", 6, 6, player1)
# #displayBoard(player1,player2)
# player1.movePiece("Q", 5, 1, player2)
# player2.movePiece("n1", 6, 3, player1)
# #displayBoard(player1,player2)
# player1.movePiece("Q", 7, 3, player2)
# displayBoard(player1, player2)
# # player2.movePiece("k", 7, 7, player1)
# # displayBoard(player1, player2)



