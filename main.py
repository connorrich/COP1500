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

# Creating the deck and player & dealer hands
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
playerHand = []
dealerHand = []
player = True
dealer = True

def Game():
    print(
        "##########################################\n           Welcome To Blackjack\n      The Goal is to beat the" +
        " dealer\n##########################################")

Game()


# Dealing hand function

def dealHand(turn):
    card = random.choice(deck)
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
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
    if dealerHand[0] == "A" or 14:
        insurance = input("Would you like insurance for a double of your bet? (y/n)")
        if insurance == 'y':
            if handTotal(dealer) == 21:
                print("Dealer has blackjack.")
                    #Need to find a way to call back to the beginning of the game and deal new hands
                    #Also figure out why this isnt displaying when dealer has an Ace
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

for i in range(2):
        dealHand(playerHand)
        dealHand(dealerHand)


while player or dealer:
        print(f"Dealer has {showDealerHand()}")
        print(f"You have {playerHand}")
        playerAction = input("What is your action\nStay, Hit, Fold (s/h/f)")
        if player:
            if playerAction == "s":
                player = True
                print(f"You have {playerHand}")
            elif playerAction == "h":
                player = True
                dealHand(playerHand)
                print(f"You have {playerHand}")
            elif playerAction == "f":
                player = False
                print("Dealer wins... dealing next hand.")
            else:
               print("Please enter a valid action")
        if handTotal(dealerHand) > 16:
            dealer = False
        else:
            dealHand(dealerHand)

        if playerAction == "s":
            player = True
        elif playerAction == "h":
            player = True
            dealHand(playerHand)
        elif playerAction == "f":
            player = False
        else:
            print("Please enter a valid action")


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
window.mainloop()
