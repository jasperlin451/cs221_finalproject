from othello import *
import greedy
import heuristics
from copy import *
from collections import *

depth = 3
def minimax(othello, cur_depth):
    if cur_depth == 0 or len(othello.validMoves) == 0:
        return othello.current_score
    worst = float('inf')
    for move in othello.validMoves:
        simulation = deepcopy(othello)
        simulation.executeMove(move)
        score = minimax(simulation, cur_depth - 1)
        if score < worst:
            worst = score 
    return worst 

def score(othello, spot):
    simulation = deepcopy(othello)
    simulation.executeMove(spot)
    return minimax(simulation, depth)

'''
total = 0
trials = 20
for i in range(trials):
    game = Othello(4)
    while len(game.validMoves) != 0:
        if (game.current):
            game.findBestMove(score)
        else:
            game.findBestMove(heuristics.score)
    total += int(game.current_score > 0)
    print total * 1.0 / (i+1)
'''
playVersusHuman(4, score)
