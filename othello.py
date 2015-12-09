from random import *
import sys
from time import sleep

class Othello:
    def __init__(self, n, states):
        self.board = {}
        self.size = n
        self.validMoves = set()
        self.current = True
        self.current_score = 0
        self.stateCounter = states

        # intialize board state
        for x in range(n):
            for y in range(n):
                self.board[(x,y)] = ' '
        self.board[(n/2-1, n/2-1)] = 'X'
        self.board[(n/2-1, n/2)] = 'O'
        self.board[(n/2, n/2-1)] = 'O'
        self.board[(n/2, n/2)] = 'X'
        for i in range(n/2-1, n/2+1):
            for j in range(n/2-1, n/2+1):
                self.addValidMoves((i, j))

    def drawBoard(self):
        # This function prints out the board that it was passed. Returns None.
        HLINE = '  '
        START = '    '
        for i in range(self.size):
            HLINE += '+----'
            START += str(i) + '    '
        HLINE += '+'
        print START
        print HLINE
        for y in range(self.size):
            print y,
            for x in range(self.size):
                print '| %s ' % (self.board[(x,y)]),
            print('|')
            print(HLINE)
        print "Score = " + str(self.current_score)

    def addValidMoves(self, spot):
        x = spot[0]
        y = spot[1]
        for i in xrange(x-1,x+2):
            for j in xrange(y-1,y+2):
                if (i,j) not in self.board or self.board[(i,j)] != ' ':
                    continue
                self.validMoves.add((i, j))

    # Helper function for possiblyFlip, dont need to call this individually
    def flipInDir(self, x, y, x_change, y_change, change, to_find, change_to):
        x += x_change
        y += y_change

        # figure to flip in the current direction
        flipped = 0
        while (x, y) in self.board and self.board[(x, y)] == to_find:
            flipped += 2
            x += x_change
            y += y_change
        if (x, y) not in self.board or self.board[(x,y)] == ' ':
            return 0
        elif not change:
            return flipped
        left = flipped
        while left > 0:
            left -= 1
            x -= x_change
            y -= y_change
            self.board[(x, y)] = change_to
        return flipped

    # if change is True, it will flip the spots in addition to counting, if
    # set to false, will simply return the number of tiles that would be
    # flipped by the move
    def possiblyFlip(self, spot, change):
        flipped = 1
        to_find = 'X'
        if self.current:
            to_find = 'O'
        x = spot[0]
        y = spot[1]

        # try out every possible direction to see what we can flip
        flipped += self.flipInDir(x, y, -1, -1, change, to_find, self.board[spot])
        flipped += self.flipInDir(x, y, -1, 0, change, to_find, self.board[spot])
        flipped += self.flipInDir(x, y, -1, 1, change, to_find, self.board[spot])
        flipped += self.flipInDir(x, y, 0, -1, change, to_find, self.board[spot])
        flipped += self.flipInDir(x, y, 0, 1, change, to_find, self.board[spot])
        flipped += self.flipInDir(x, y, 1, -1, change, to_find, self.board[spot])
        flipped += self.flipInDir(x, y, 1, 0, change, to_find, self.board[spot])
        flipped += self.flipInDir(x, y, 1, 1, change, to_find, self.board[spot])
        return flipped

    # Call to move to the next turn
    def nextTurn(self):
        self.current = not self.current

    # Called by findBestMove, don't call by itself (except by human)
    def executeMove(self, spot):
        self.validMoves.remove(spot)
        if self.current:
            self.board[spot] = 'X'
        else:
            self.board[spot] = 'O'
        score_diff = self.possiblyFlip(spot, True)
        if self.current:
            self.current_score += score_diff
        else:
            self.current_score -= score_diff

    # Generic function that takes in the scoring function to use
    def findBestMove(self, scoringFunction):
        best = float("-inf")
        best_move = None
        # greedily selects the move resulting in the largest number of flipped tiles
        shuffled_moves = list(self.validMoves)
        shuffle(shuffled_moves)
        for play in shuffled_moves:
            current_score = scoringFunction(self, play)
            if current_score > best:
                best = current_score
                best_move = play
            if not self.current:
                break

        # play the best move
        self.executeMove(best_move)
        self.addValidMoves(best_move)

def playVersusHuman(size, sf):
    game = Othello(size, dict())
    while len(game.validMoves) != 0:
        if (game.current):
            game.findBestMove(sf)
            game.drawBoard()
        else:
            print "Spot to play on:"
            move = tuple(int(x.strip()) for x in raw_input().split(',')) 
            game.executeMove(move)
            game.addValidMoves(move)
            game.drawBoard()
        game.nextTurn()







