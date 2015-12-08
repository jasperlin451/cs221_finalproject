from othello import *

def score(othello, spot):
    return othello.possiblyFlip(spot, False)
    
total = 0
for i in range(200):
    total += playFullGame(8, score)
print total / 200.0
