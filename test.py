from player import *
from pieces import *


player1 = Player("Charles", "W")
player2 = Player("Harry", "B")
player1.movePiece("P2" , 4, 2, player2)
player1.movePiece("P3" , 4, 3, player2)
player2.movePiece("p4", 5, 4, player1)
r = player2.movePiece("q", 4, 1, player1)
r = player2.movePiece("p4", 4, 3, player1)
displayBoard(player1, player2)
print(r)

