
import random

def gameGuess(num):
    while True:
        try: guess = int(raw_input("What's your guess? "))
        except ValueError:
            print "Please enter an integer from 1 to 100."
        break

    if guess == num:
        print "You've guessed correctly!"
        return True
    elif guess < num:
        print "The number is higher than your guess of " + str(guess)
    else:
        print "The number is lower than your guess of " + str(guess)

def playGame():
    num = random.randint(1,100)
    print ""
    print "I'm thinking of a number between 1 and 100."
    print "You have 5 guesses."
    print ""

    i = 0
    winCondition = False
    while i < 5 and not winCondition:
        i += 1
        winCondition = gameGuess(num)

    if i == 5 and not winCondition:
        print ""
        print "You're all out of guesses!"
        print ""
        print "The number was " + str(num)

playGame()
