"""
Connor Richardson
COP 1500
Prof. Osheroff

This is a early form of a blackjack game
I will be trying to add on further hands, being able to play more than one hand.
Also potentially trying to add multiple deck games like 6 or 3 deck games with legitmate card elimination
https://www.w3schools.com/python/python_classes.asp <---- this helped with looking into classes
https://gist.github.com/athiyadeviyani/b18afdc8136f003956b1a71d94a6c696 <---- also looked into this for tkinter GUI
"""
from tkinter import *
import random

# Creates window and title
window = Tk()
window.title("Blackjack")
window.geometry('1000x1000')
lbl = Label(window, text="Hello, Welcome to Blackjack!", font=("Times New Roman", 20))
lbl.grid(column=250, row=250)


def Game():
    print(
        "##########################################\n           Welcome To Blackjack\n      The Goal is to beat the" +
        " dealer\n##########################################")


Game()

# Creating the deck and player & dealer hands
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
playerHand = []
dealerHand = []
playerTurn = True
dealerTurn = True


# Creating new deck if deck runs out
def checkDeck(deck):
    if len(deck) == 0:
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    else:
        return deck


# Dealing hand function

def dealHand(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


# Calculating the total of the dealer and players hands

def handTotal(turn):
    total = 0
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card == "J" or card == "Q" or card == "K":
            total += 10
        else:
            total += 11
    return total


# Showing only one of the dealer cards

def showDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    if dealerHand[0] == "A":
        insurance = input("Would you like insurance for a double of your bet? (y/n)")
        if insurance == 'y':
            if handTotal(dealerHand) == 21:
                print("Dealer has blackjack.")
    # Need to find a way to call back to the beginning of the game and deal new hands
    elif len(dealerHand) > 2:  # This basically means that it is the dealers turn
        return dealerHand[0], dealerHand[1]


for i in range(2):
    dealHand(playerHand)
    dealHand(dealerHand)


def main(playerTurn, dealerTurn):
    while playerTurn or dealerTurn:
        print(f"Dealer has {showDealerHand()}")
        print(f"You have {playerHand}")
        playerAction = input("What is your action\nStay, Hit, Fold (s/h/f)")
        if playerAction == "s":
            playerTurn = False
            print(f"Dealer has {handTotal(dealerHand)}")
            print(f"You have {handTotal(playerHand)}")
        elif playerAction == "h":
            playerTurn = True
            dealHand(playerHand)
            if handTotal(playerHand) > 21:
                print("You busted... dealing next hand")
                dealerHand.clear()
                playerHand.clear()
            else:
                print(playerHand)
        elif playerAction == "f":
            playerTurn = False
            print("##########################################\n         Dealer wins... dealing next hand." +
                  "\n##########################################")
            dealerHand.clear()
            playerHand.clear()
            for i in range(2):
                dealHand(playerHand)
                dealHand(dealerHand)
        else:
            print("Please enter a valid action")


main(playerTurn, dealerTurn)
"""
CashBalance = float(input("Enter in your buy in: "))
HandsLeft = CashBalance // 2
print("Minimum hands left to play: ", + HandsLeft)
"""

# Also need to learn how to import all of these print functions into display in the Tkinter modules

"""
Need to put this into its own function
HandWin = CashBalance + HandOutcome
HandLose = CashBalance - HandOutcome

#Example Jackpot to demonstrate exponential
print(CashBalane ** 2)

#This will print the balance left after paying X amount of hands
print(CashBalance % 2)
x = 15/2
print(x)
print("Software", "Development", sep = '')
print("Study", "play", sep = ' and ')

"""

# this makes the GUI window appear
# window.mainloop()
