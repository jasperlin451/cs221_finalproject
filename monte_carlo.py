from random import *
from othello import *
from copy import *
from collections import *
import greedy

def simulate(othello, n):
    for i in range(n):
        simulation = deepcopy(othello) 
        moves = [hash(frozenset(othello.board.items()))]
        while len(simulation.validMoves) != 0:
            move = choice(list(simulation.validMoves))
            simulation.executeMove(move)
            simulation.addValidMoves(move)
            boardHash = hash(frozenset(simulation.board.items()))
            moves.append(boardHash)
        for h in moves:
            if (h not in othello.stateCounter):
                othello.stateCounter[h] = (0, 0)
            cs = othello.stateCounter[h]
            othello.stateCounter[h] = (cs[0] + 1, cs[1] + simulation.current_score)

def score(othello, spot):
    simulation = deepcopy(othello) 
    simulation.executeMove(spot)
    boardHash = hash(frozenset(simulation.board.items()))
    if boardHash not in othello.stateCounter:
        return 0
    return othello.stateCounter[boardHash][1] * 1.0 / othello.stateCounter[boardHash][0]

total = 0
trials = 50
states = dict()
for i in range(trials):
    game = Othello(4, states) 
    while len(game.validMoves) != 0:
        simulate(game, 10)
        if (game.current):
            game.findBestMove(score)
        else:
            game.findBestMove(greedy.score)
    total += int(game.current_score > 0)
    states = game.stateCounter
print total * 1.0 / trials

playVersusHuman(4, score)
