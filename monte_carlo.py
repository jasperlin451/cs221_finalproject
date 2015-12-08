from othello import *

def score(othello, spot):
    print "hi" 

total = 0
for i in range(200):
    total += playFullGame(4, score)
print total / 200.0
