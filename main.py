"""
Connor Richardson
COP 1500
Prof. Osheroff

This is a early form of a blackjack game

This helped with learning
https://www.w3schools.com/python/
"""

import random

# Creating the deck and player & dealer hands
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
playerHand = []
dealerHand = []
playerTurn = True
dealerTurn = True
aceSoft = False

def checkDeck():
    """
    Creating new deck if deck runs out
    """
    global deck
    if len(deck) <= 20:
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4



def hit(turn):
    """
    Dealing hand function
    :param turn: the turn of the player
    :return: card that was removed from the deck and added to the turns hand
    """
    global deck
    global aceSoft

    checkDeck()

    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
    """
    This was one of the hardest things 
    to try and implement into the game
    """
    if handTotal(turn) > 21 and 'A' in turn and not aceSoft:
        aceSoft = True
    return card


def dealHand():
    """
    Deals players hands as a function
    """
    global dealerHand
    global playerHand
    dealerHand.clear()
    playerHand.clear()
    hit(playerHand)
    hit(dealerHand)
    hit(playerHand)
    hit(dealerHand)



def handTotal(turn):
    """
    Calculating the total of the dealer and players hands
    :param turn: the turn of the player
    :return: the total of the players hand
    """
    global aceSoft
    total = 0
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card == "J" or card == "Q" or card == "K":
            total += 10
        elif aceSoft:
            total += 1
        else:
            total += 11
    return total


def showDealerHand():
    """
    This function will check for insurance and will only how one of the dealers cards
    :return: the first card that the dealer has
    """
    global dealerHand

    if len(dealerHand) == 2:
        return dealerHand[0]
    if dealerHand[0] == "A":
        insurance = input("Would you like insurance for a double of your bet? (y/n)")
        if insurance == 'y':
            if handTotal(dealerHand) == 21:
                print("Dealer has blackjack.")
    # Need to find a way to call back to the beginning of the game and deal new hands
    else:  # len(dealerHand) > 2  # This basically means that it is the dealers turn
        return dealerHand[0]


def Game():
    """
    This is the game function
    """
    global playerTurn
    global dealerTurn

    dealHand()
    while playerTurn or dealerTurn:
        print(f"Dealer has {showDealerHand()}")
        print(f"You have {str(playerHand)[1:-1]}")
        if handTotal(playerHand) == 21:
            print("You have blackjack!!!!!!!!!!!\n")
            print("Dealing next hand...\n")
            dealHand()
        else:
            playerAction = input("\nStay or Hit (s/h): ")
            if playerAction == "s":
                playerTurn = False
                print(f"Dealer has {handTotal(dealerHand)}")
                print(f"You have {handTotal(playerHand)}\n")
                print("Dealing next hand...\n")
                dealHand()
            elif playerAction == "h":
                checkDeck()
                print(f"You got the a {hit(playerHand)}")
                if handTotal(playerHand) > 21:
                    print("You busted... dealing next hand\n")
                    checkDeck()
                    dealHand()
            else:
                print("Please enter a valid action")


def main():
    print(
        "##########################################\n           Welcome To Blackjack\n      The Goal is to beat the" +
        " dealer\n##########################################")
    Game()


main()