
import random

print ""
print "Welcome to Mike's BlackJack Game"
print ""

money = 100

def dealCard():
    card = random.randint(1,13)
    return card

def valueCard(card):
    if card in [11, 12, 13]:
        return 10
    else:
        return card

def strCard(card):
    if card == 1:
        return "A"
    elif card == 11:
        return "J"
    elif card == 12:
        return "Q"
    elif card == 13:
        return "K"
    else:
        return str(card)

def playBet(money):
    while True:
        bet = int(raw_input("How much would you like to bet? "))
        if bet > money:
            print "You do not have enough money!"
        else:
            print "You bet " + str(bet)
            break
    return bet

def playAgain(money):
    print ""
    decision = raw_input("Would you like to play again? ").upper()
    if decision == "YES":
        playGame(money)
    else:
        print ""
        print "Thanks for playing!"

def playGame(money):
    print "You have $" + str(money) + " to bet."
    print ""

    handBet = playBet(money)

    dealer = 0
    player = 0

    # first round of cards dealt
    dealerFirst = dealCard()
    dealer += valueCard(dealerFirst)
    playerFirst = dealCard()
    player += valueCard(playerFirst)
    print "You've been dealt a " + strCard(playerFirst)
    print ""

    # second round of cards dealt
    dealerSecond = dealCard()
    print "Dealer shows a " + strCard(dealerSecond)
    dealer += valueCard(dealerSecond)
    playerSecond = dealCard()
    player += valueCard(playerSecond)
    print "You've been dealt a " + strCard(playerSecond)
    print "You now are at " + str(player)
    print ""

    playerHits = raw_input("Would you like to hit? ").upper()
    playerBusted = False
    while playerHits == "YES":
        playerCard = dealCard()
        player += valueCard(playerCard)
        print "You've been dealt a " + strCard(playerCard)
        print "You now are at " + str(player)
        print ""
        if player > 21:
            playerBusted = True
            print "You've busted!"
            money -= handBet
            playerHits = "NO"
        else:
            playerHits = raw_input("Would you like to hit again? ").upper()

    dealerBusted = False
    if not playerBusted:
        print "Dealer's face-down card was a " + strCard(dealerFirst)
        print "Dealer is at " + str(dealer)
        while dealer < 17:
            dealerCard = dealCard()
            dealer += valueCard(dealerCard)
            print "Dealer receives a " + strCard(dealerCard)
            print "Dealer is at " + str(dealer)
            print ""
            if dealer > 21:
                dealerBusted = True
                print "Dealer busts!"
                money += handBet
        if not dealerBusted:
            if player > dealer:
                print "You win!"
                money += handBet
            elif player == dealer:
                print "It's a push!"
            else:
                print "Dealer wins!"
                money -= handBet

    if money == 0:
        print "You've run out of money!"
    else:
        playAgain(money)

playGame(money)
