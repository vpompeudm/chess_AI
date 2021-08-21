from board import Board
from pieces import Pieces
from chess_game import ChessGame

board = Board()
pieces = Pieces()
game = ChessGame(board, pieces)

checkmate = False
draw = False

while not checkmate and not draw:

    game.board.print_board('white')
    response = 'waiting'
    while response != 'Ok':
        white_move = input('White to move: ')
        response = game.move_piece('W'+white_move)
        print (response)
        
    game.board.print_board('black')
    response = 'waiting'
    while response != 'Ok':
        black_move = input('Black to move: ')
        response = game.move_piece('B'+black_move)
        print (response)