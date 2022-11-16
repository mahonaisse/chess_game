class menu(ChessGame):

while True:
  try:
    typeGame = int(input("Enter 1 for New Game, 2 for Load Game, or 3 for Play Custom Games")) 
    if typeGame=='1':
      print("New Game entered successfully")
      break
    elif typeGame=='2':
        print("Load Game entered successfully")
        break
    elif typeGame=='3':
        print("Play Custom Games entered successfully")
        break
    else:
      print("Enter 1, 2 or 3")      
  except ValueError:
    print("Provide an integer value...")
    continue