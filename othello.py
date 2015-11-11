import random
import sys

class othello:
    def __init__(self):
        self.board = {}
        for x in range(8):
            for y in range(8):
                self.board[(x,y)] = ' '
        #starting
        self.board[(3, 3)] = 'X'
        self.board[(3, 4)] = 'O'
        self.board[(4, 3)] = 'O'
        self.board[(3, 4)] = 'X'
        self.currentTile = 'X'

    def drawBoard(self):
        # This function prints out the board that it was passed. Returns None.
        HLINE = '  +---+---+---+---+---+---+---+---+'
        VLINE = '  |   |   |   |   |   |   |   |   |'
        print '    1   2   3   4   5   6   7   8'
        print HLINE
        for y in range(8):
            print VLINE
            print y + 1,
            for x in range(8):
                print '| %s' % (self.board[(x,y)]),
                print '|'
                print(VLINE)
                print(HLINE)

    def isValidMove(self, ):

    def getValidMoves(self):
        validMoves = []
        for x in range(8):
            for y in range(8):
                if self.isValidMove(self, ) != False:
                    validMoves.append([x,y])
        return validMoves

    def getScoreOfBoard(self):
        xscore = 0
        oscore = 0
        for x in range(8):
            for y in range(8):
                if self.board[(x, y)] == 'X':
                    xscore += 1
                if self.board[(x,y)] == 'O':
                    oscore += 1
        return {'X': xscore, 'O': oscore}



