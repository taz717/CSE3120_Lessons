'''
Moataz Khallaf A.K.A Hackerman
03-RPC
3/20/2019
'''
import random

### Classes
class RPS:
    def __init__(self, choice):
        self.choice = choice
        self.objDic = {
            1: "rock",
            2: "paper",
            3: "scissor",
        }
    def inputRPS(self):
        return self.objDic[self.choice]
    def __str__(self):
        return self.objDic[self.choice]

class game:
    def __init__(self, player1, player2):
        self.resultDic = {
            "rockscissor": "win",
            "scissorpaper": "win",
            "paperrock": "win",
            "rockpaper": "lost",
            "paperscissor": "lost",
            "scissorrock": "lost",
            "paperpaper": "tie",
            "scissorscissor": "tie",
            "rockrock": "tie"
        }
        self.choice1 = player1
        self.choice2 = player2
        self.check = self.choice1+self.choice2
        self.player1score = score1
        self.player2score = score2
    def result(self):
        return self.resultDic[self.check]
    def score(self, score1, score2):
        if self.resultDic[self.check] == "win":
            score1 += 1
        elif self.resultDic[self.check] == "lost":
            score2 += 2
        return score1, score2

###vars
score1 = 0
score2 = 0

player1 = RPS(int(input("rock(1),paper(2),Scissor(3) ")))
player2 = RPS(random.randrange(1, 4))
play = game(player1.inputRPS(), player2.inputRPS())

###Outputs
print(player1, player2)
print(play.result(), play.score(score1, score2))