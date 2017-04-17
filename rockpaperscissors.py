
import random

def playerTurn():
    while True:
        playerMove = raw_input("Do you pick 'rock', 'paper', or 'scissors?' ").upper()
        if playerMove in ["ROCK", "PAPER", "SCISSORS"]:
            break
    print ""
    print "Player plays " + playerMove + "!"
    return playerMove

def compTurn():
    compMove = random.randint(1,3)
    if compMove == 1:
        print "Computer plays ROCK!"
    elif compMove == 2:
        print "Computer plays PAPER!"
    else:
        print "Computer plays SCISSORS!"
    return compMove

def evaluateGame(playerMove, compMove):
    print ""
    if playerMove == "ROCK":
        if compMove == 1:
            print "It's a tie!"
        elif compMove == 2:
            print "Computer wins!"
        else:
            print "Player wins!"
    if playerMove == "PAPER":
        if compMove == 1:
            print "Player wins!"
        elif compMove == 2:
            print "It's a tie!"
        else:
            print "Computer wins!"
    if playerMove == "SCISSORS":
        if compMove == 1:
            print "Computer wins!"
        elif compMove == 2:
            print "Player wins!"
        else:
            print "It's a tie!"

def playAgain():
    print ""
    decision = raw_input("Would you like to play again? ").upper()
    if decision == "YES":
        playGame()
    else:
        print ""
        print "Thanks for playing!"

def playGame():
    print ""
    print "Welcome to Mike's Rock, Paper, Scissors game!"
    print ""

    playerMove = playerTurn()
    compMove = compTurn()
    evaluateGame(playerMove, compMove)
    playAgain()

playGame()
