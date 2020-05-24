'''
Moataz Khallaf A.K.A Hackerman
01-diceClass
3/14/2019
'''
import random

class die:
    def __init__(self, sides):
        self.sides = sides
        self.values = [ ]
        self.setNumSides(sides)

    def getRollVal(self):
        return self.values[random.randrange(len(self.values))]

    def setNumSides(self, sides):
        self.sides = sides
        self.setSideVal(self.sides)

    def getSideNum(self):
        return self.sides

    def setSideVal(self, size):
        tempList = [1, 2, 3, 4, 5, 6]
        '''
        for i in range(size):
            tempList.append(int(input(" value ")))
            '''
        self.values = tempList

class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dice = [die(6), die(6), die(6), die(6)]

    def getScore(self):
        return self.score

    def calcScore(self):
        for i in range(len(self.dice)):
            self.score += self.dice[i].getRollVal()

taz = player('taz')
taz.calcScore()
print(taz.getScore())

'''
#d1 = die() #constructing our object from the class
d2 = die(4)
print(d1.getSideNum(), d2.getSideNum())

#d1.setNumSides(3)
d2.setNumSides(4)

print(d1.getSideNum(), d2.getSideNum())

#d2.setSideVal(d2.getSideNum())
print(d2.getRollVal())
'''