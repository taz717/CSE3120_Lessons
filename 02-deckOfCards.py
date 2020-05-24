'''
Moataz Khallaf A.K.A Hackerman
02-deckOfCards
3/15/2019
'''

class card:
    number = {
        1 : "Ace",
        2 : "Two",
        3 : "Three",
        4 : "Four",
        5 : "Five",
        6 : "Six",
        7 : "Seven",
        8 : "Eight",
        9 : "Nine",
        10 : "Ten",
        11 : "Jack",
        12 : "Queen",
        13 : "King"
    }
    suits = {
        0 : "Diamonds",
        1 : "Clubs",
        2 : "Hearts",
        3 : "Spades"
    }

    def __init__(self, value, suits):
        self.value = value
        self. suit = suits

    def __str__(self):
        return self.number[self.value] + " of " + self.suits[self.suit]

class deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(1, 14):
                self.cards.append(card(j, i))

    def drawRandCard(self):  # setter method
        from random import randrange
        return self.cards.pop(randrange(len(self.cards)))

    def getDeckSize(self):  # getter method
        return len(self.cards)

class player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def addCard(self, obj):  # setter method
        self.hand.append(obj)
        return self.hand

    def getHand(self):
        tempHand  = []
        for i in range(len(self.hand)):
            tempHand.append(str(self.hand[i]))
        strHand = ", ".join(tempHand)
        return self.name + "'s hand: " + strHand

    def __repr__(self):
        return self.hand

myDeck = deck()
player1 = player("Taz")

#interface
player1.addCard(myDeck.drawRandCard())
print(player1.getHand())

print(player1)
print(myDeck.getDeckSize())