
# Write a program that lets two humans play a game of Tic Tac Toe in a terminal.
# The program should let the players take turns to input their moves.
# The program should report the outcome of the game.
#
# You will pair on adding support for a computer player to your game.
# You can start with random moves and make the AI smarter if you have time.

import random

# Draws the board
def drawBoard(board):
    print ""
    print " %s | %s | %s " % (board[1], board[2], board[3])
    print "-----------"
    print " %s | %s | %s " % (board[4], board[5], board[6])
    print "-----------"
    print " %s | %s | %s " % (board[7], board[8], board[9])
    print ""

# Checks to see if specific board position is occupied
def isOccupied(pos, board):
    return (board[pos] in ["X", "O"])

# Player move function
def playerMove(board, symbol):
    while True:
        try: pos = int(raw_input("Player turn:  where would you like to play? "))
        except ValueError:
            print "This is an invalid move."
            print "Please enter an integer from 1 to 9."
        if not isOccupied(pos, board):
            break
    board[pos] = symbol
    return board

# Computer move function
def computerMove(board, symbol):
    while True:
        if not isOccupied(5, board):
            compMove = 5
        elif not isOccupied(1, board) and ((board[2] == board[3]) or (board[4] == board[7]) or (board[5] == board[9])):
            compMove = 1
        elif not isOccupied(2, board) and ((board[1] == board[3]) or (board[5] == board[8])):
            compMove = 2
        elif not isOccupied(3, board) and ((board[1] == board[2]) or (board[6] == board[9] ) or (board[5] == board[7])):
            compMove = 3
        elif not isOccupied(4, board) and ((board[5] == board[6]) or (board[1] == board[7])):
            compMove = 4
        elif not isOccupied(5, board) and ((board[4] == board[6]) or (board[2] == board[8]) or (board[1] == board[9]) or (board[3] == board[7])):
            compMove = 5
        elif not isOccupied(6, board) and ((board[4] == board[5]) or (board[3] == board[9])):
            compMove = 6
        elif not isOccupied(7, board) and ((board[8] == board[9]) or (board[1] == board[4]) or (board[3] == board[5])):
            compMove = 7
        elif not isOccupied(8, board) and ((board[7] == board[9]) or (board[2] == board[5])):
            compMove = 8
        elif not isOccupied(9, board) and ((board[7] == board[8]) or (board[3] == board[6]) or (board[1] == board[5])):
            compMove = 9
        else:
            compMove = random.randint(1, 9)
        if not isOccupied(compMove, board):
            break
    board[compMove] = symbol
    return board

# Checks to see if there is a winner
def checkWinner(board, sym):
    return ((board[1], board[2], board[3]) == (sym, sym, sym) or
        (board[4], board[5], board[6]) == (sym, sym, sym) or
        (board[7], board[8], board[9]) == (sym, sym, sym) or
        (board[1], board[4], board[7]) == (sym, sym, sym) or
        (board[2], board[5], board[8]) == (sym, sym, sym) or
        (board[3], board[6], board[9]) == (sym, sym, sym) or
        (board[7], board[5], board[3]) == (sym, sym, sym) or
        (board[9], board[5], board[1]) == (sym, sym, sym))

# Game mode vs another human player
def vsHuman():
    board = ["","1","2","3","4","5","6","7","8","9"]
    gameDone = False
    symbol = "O"
    turn = 0

    drawBoard(board)

    while gameDone == False:
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"
        
        board = playerMove(board, symbol)
        drawBoard(board)
        turn += 1

        if checkWinner(board, symbol):
            print symbol + " wins!"
            gameDone = True
        elif turn == 9:
            print "It's a tie!"
            gameDone = True

# Game mode vs computer
def vsComputer():
    board = ["","1","2","3","4","5","6","7","8","9"]
    gameDone = False
    symbol = "X"
    turn = 0

    drawBoard(board)

    while gameDone == False:
        if symbol == "X":
            board = playerMove(board, "X")
            drawBoard(board)
            turn += 1
        else:
            board = computerMove(board, "O")
            print "\nComputer plays a spot!"
            drawBoard(board)
            turn += 1
        
        if checkWinner(board, symbol):
            print symbol + " wins!"
            gameDone = True
        elif turn == 9:
            print "It's a tie!"
            gameDone = True
        
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"

# Decide to play against either a human or a computer
def decideGameMode():
    while True:
        gameMode = raw_input("Would you like to play against a 'human' or 'computer'? ").upper()
        if gameMode in ["HUMAN", "COMPUTER"]:
            break

    if gameMode == "HUMAN":
        vsHuman()
    else:
        vsComputer()

# Decide whether or not to play another game
def decidePlayAgain():
    playAgain = raw_input("\nWould you like to play again? ").upper()

    if playAgain == "YES":
        playGame()
    else:
        print "Thanks for playing!"

# Main game loop
def playGame():
    decideGameMode()
    decidePlayAgain()

# Introductory print statement
print "\nWelcome to Mike's Tic-Tac-Toe game!\n"

# Enter main game loop 
playGame()
