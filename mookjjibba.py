
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
        compMove = "ROCK"
        print "Computer plays ROCK!"
    elif compMove == 2:
        compMove = "PAPER"
        print "Computer plays PAPER!"
    else:
        compMove = "SCISSORS"
        print "Computer plays SCISSORS!"
    return compMove

def evaluateRPS(playerMove, compMove):
    print ""
    if playerMove == "ROCK":
        if compMove == "ROCK":
            print "It's a tie!"
        elif compMove == "PAPER":
            print "Computer has the advantage!"
            return "COMP"
        else:
            print "Player has the advantage!"
            return "PLAYER"
    if playerMove == "PAPER":
        if compMove == "ROCK":
            print "Player has the advantage!"
            return "PLAYER"
        elif compMove == "PAPER":
            print "It's a tie!"
        else:
            print "Computer has the advantage!"
            return "COMP"
    if playerMove == "SCISSORS":
        if compMove == "ROCK":
            print "Computer has the advantage!"
            return "COMP"
        elif compMove == "PAPER":
            print "Player has the advantage!"
            return "PLAYER"
        else:
            print "It's a tie!"

def mjb(rpsWinner):
    playerMove = playerTurn()
    compMove = compTurn()
    result = evaluateMJB(playerMove, compMove)
    if result == "WIN":
        print rpsWinner + " wins!"
    else:
        print result + " has the advantage."
        print ""
        mjb(result)

def evaluateMJB(playerMove, compMove):
    print ""
    if playerMove == "ROCK":
        if compMove == "ROCK":
            return "WIN"
        elif compMove == "PAPER":
            return "Computer"
        else:
            return "Player"
    if playerMove == "PAPER":
        if compMove == "ROCK":
            return "Player"
        elif compMove == "PAPER":
            return "WIN"
        else:
            return "Computer"
    if playerMove == "SCISSORS":
        if compMove == "ROCK":
            return "Computer"
        elif compMove == "PAPER":
            return "Player"
        else:
            return "WIN"

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
    print "Welcome to Mike's Mook-Jji-Bba game!"
    print ""

    rpsWinner = "null"
    while rpsWinner not in ["PLAYER", "COMP"]:
        playerMove = playerTurn()
        compMove = compTurn()
        rpsWinner = evaluateRPS(playerMove, compMove)
        print ""

    mjb(rpsWinner)
    playAgain()

playGame()
