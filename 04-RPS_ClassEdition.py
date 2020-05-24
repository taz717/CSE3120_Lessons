'''
Moataz Khallaf A.K.A Hackerman
04-RPS_ClassEdition
3/22/2019
'''
import random

# Objects


class thing:
    def __init__(self, name, ):
        selection = ["rock", "paper", "scissor"]
        beats = {
            "rock" : "scissor",
            "paper" : "rock",
            "scissor" : "paper",
        }
        self.name = selection[name]
        self.defeats = beats[self.name]

    def getName(self):
        return self.name

    def getDefeat(self):
        return self.defeats

    def __str__(self):
        return self.name


class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getChoice(self):
        return self.choice

    def setChoice(self, choice):
        self.choice = thing(choice)

    def addScore(self):
        self.score += 1

# Functions


def menu():
    print('''
    1) rock
    2) paper
    3) scissors
    4) exit
    ''')
    choice = int(input("> "))
    if choice == 4:
        exit()
    choice -= 1
    return choice


def findWinner(play1, play2):
    if play1.getChoice().getName() == play2.getChoice().getName():
        return 0
    elif play1.getChoice().getDefeat() == play2.getChoice().getName():
        play1.addScore()
        return 1
    elif play1.getChoice().getName() == play2.getChoice().getDefeat():
        play2.addScore()
        return 2


def displayWin(result, play1, play2):
    # print player choices
    print("%s chose %s." % (play1.getName(), play1.getChoice()))  # percent s works no matter what
    print(f'{play2.getName()} chose {play2.getChoice()}')  # f strings only work < python 3.5
    # print actual result
    if result == 0:
        print("tie")
    elif result == 1:
        print(play1.getName()+" wins")
    elif result == 2:
        print(play2.getName()+" wins")
    print(f'{play1.getName()} : {play1.getScore()} | {play2.getName()} : {play2.getScore()}')

# Main


player1 = player("Taz")
comp = player("Daj")

while True:
    select = menu()
    player1.setChoice(select)
    comp.setChoice(random.randrange(3))
    win = findWinner(player1, comp)

    displayWin(win, player1, comp)

    '''
functions are the pathways objects use to interact with each other.
objects are the data stored and their interactions. so a function helps an object
interact with other objects but doesn't modify it at all.    
'''