from othello import *
import random
import rand_move

def score(othello, spot):
    return othello.possiblyFlip(spot, False)
    
total = 0
for i in range(200):
    game = Othello(4)
    while len(game.validMoves) != 0:
        if (game.current):
            game.findBestMove(score)
        else:
            game.findBestMove(rand_move.score)
    total += int(game.current_score > 0)
# print total / 200.0
