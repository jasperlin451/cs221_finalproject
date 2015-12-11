from othello import *
from copy import *
import greedy
import minimax

def numCornerPieces(prev, spot):
    game = deepcopy(prev)
    game.executeMove(spot)
    corners = 0
    to_find = 'X'
    if not game.current:
        to_find = 'O'
    if game.board[(0, 0)] == to_find:
        corners += 1
    if game.board[(game.size-1, 0)] == to_find:
        corners += 1
    if game.board[(game.size-1, game.size-1)] == to_find:
        corners += 1
    if game.board[(0, game.size-1)] == to_find:
        corners += 1
    return corners / 4.0

def mobility(game, spot):
    new_moves = 0
    x = spot[0]
    y = spot[1]
    for i in xrange(x-1,x+2):
        for j in xrange(y-1,y+2):
            if (i, j) in game.board and game.board[(i, j)] == ' ':
                new_moves += 1
    return new_moves / 7.0

def gameEnder(game, spot):
    simulation = deepcopy(game)
    simulation.executeMove(spot)
    if game.current_score == game.pieces:
        return True
    return False
    
def cornerProximity(game, spot):
    closest = 2*game.size 
    if (spot[0] + spot[1]) < closest:
        closest = spot[0] + spot[1]
    if (spot[0] + game.size - spot[1]) < closest:
        closest = spot[0] + game.size - spot[1]
    if (spot[1] + game.size - spot[0]) < closest:
        closest = spot[1] + game.size - spot[0]
    if (2*game.size - spot[0] - spot[1]) < closest:
        closest = 2*game.size - spot[0] - spot[1]
    return (2*game.size - closest) * 1.0 / 2*game.size

def scoreDifference(game, spot):
    flipped = game.possiblyFlip(spot, False)
    return flipped * 1.0 / game.pieces

corner_weight = 0.1
mobility_weight = 0.2
proximity_weight = 0.2
flip_weight = 0.5
def score(game, spot):
    if gameEnder(game, spot): return 1
    combined_score = 0
    combined_score += numCornerPieces(game, spot) * corner_weight
    combined_score += mobility(game, spot) * mobility_weight
    combined_score += cornerProximity(game, spot) * proximity_weight
    combined_score += scoreDifference(game, spot) * flip_weight
    return combined_score

total = 0
trials = 10
for i in range(trials):
    game = Othello(6)
    while len(game.validMoves) != 0:
        if (game.current):
            game.findBestMove(score)
        else:
            game.findBestMove(minimax.score)
    total += int(game.current_score > 0)
print total * 1.0 / trials
