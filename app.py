import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
    #apparently this should say, "Create a new instance of GameBoard called 'board.'"
board = gameboard.GameBoard()

# Create a new Player called played starting at position 3,2
    #apparently this should say, "Create a new instance of Player called 'player' starting at position 3,2."
player = player.Player(5, 3)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
        #figure out direction and check if move allowed
    if selection == "w" and board.checkMove(player.rowPosition - 1, player.columnPosition):
        player.moveUp()
    elif selection == "s" and board.checkMove(player.rowPosition + 1, player.columnPosition):
        player.moveDown()
    elif selection == "a" and board.checkMove(player.rowPosition, player.columnPosition - 1):
        player.moveLeft()
    elif selection == "d" and board.checkMove(player.rowPosition, player.columnPosition + 1):
        player.moveRight()
    else:
        print("This is not a valid selection! Use w, a, s or d.")
            
    # Check if the player has won, if so print a message and break the loop!
    if board.checkWin(player.rowPosition, player.columnPosition):
        board.printBoard(player.rowPosition, player.columnPosition)
        break