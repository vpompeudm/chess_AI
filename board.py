import numpy as np
from tabulate import tabulate

class Board():
    def __init__(self):
        self.board = [['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'], 
                      ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                      ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']]

    def set_square(self, square, piece):
        column = int(square[0])
        row = int(square[1])
        self.board[row][column] = piece

    def check_square(self, square):
        column = int(square[0])
        row = int(square[1])
        return self.board[row][column]
    
    def print_board(self, side):
        if side == 'white':
            print (tabulate(reversed(self.board)))
        if side == 'black':
            print(tabulate([reversed(list) for list in self.board]))
