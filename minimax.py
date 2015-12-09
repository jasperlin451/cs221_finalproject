import othello
from copy import *
from collections import *
import greedy

def minimax(othello, depth):
    if depth == 0 or len(othello.validMoves) == 0:
        return othello.current_score, None
    if othello.current:
        bestValue = -float('inf')
        bestMove = None
        for move in othello.validMoves:
            simulation = deepcopy(othello)
            simulation.executeMove(move)
            simulation.current = not simulation.current
            val, bestMove = minimax(simulation, depth)
            if val > bestValue:
                bestValue = val
                bestMove = move
        return bestValue, bestMove
    else:
        bestValue = float('inf')
        bestMove = None
        for move in othello.validMoves:
            simulation = deepcopy(othello)
            simulation.executeMove(move)
            simulation.current = not simulation.current
            val, bestMove = minimax(simulation, depth - 1)
            if val < bestValue:
                bestValue = val
                bestMove = move
        return bestValue, bestMove
