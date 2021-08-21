import numpy as np

class ChessGame():
    def __init__(self, board, pieces):
        self.board = board
        self.pieces = pieces
        
    def move_piece(self, move):
        
        current_square = np.array([0,0])
        target_square = np.array([0,0])
        
        piece_color = move[0]
        piece_type = move[1]

        current_square[0] = ord(move[2]) - 97
        current_square[1] = int(move[3]) - 1
        
        target_square[0] = ord(move[4]) - 97
        target_square[1] = int(move[5]) - 1

        if self.is_valid_move(self, piece_color, piece_type, current_square, target_square):
            self.board.set_square(current_square, '__')
            self.board.set_square(target_square, piece_color + piece_type)
            return 'Ok'                
        return 'Not a valid Move'

    @staticmethod
    def is_valid_move(self, piece_color, piece_type, current_square, target_square):
        
        if not self.is_square_valid(current_square) or not self.is_square_valid(target_square):
            print ('Not a valid square')
            return False
        
        if self.is_square_occupied(self, piece_color, target_square):
            print ('Square occupied')
            return False
        
        if not self.is_piece_on_board(self, piece_color, piece_type, current_square):
            print ('Piece not found')
            return False

        is_capture = self.is_capture(self, piece_color, target_square)

        if not self.pieces.is_valid_piece_move(piece_color, piece_type, current_square, target_square, is_capture):
            print ('Not a valid piece move')
            return False

        if self.is_piece_obstructed(self, current_square, target_square) and piece_type != 'N':
            print ('Move obstructed')
            return False
        
        if not self.is_legal():
            return False

        return True

    @staticmethod
    def is_square_valid(square):
        if any(i<0 for i in square) or any(i>7 for i in square):
            return False
        return True

    @staticmethod
    def is_square_occupied(self, piece_color, target_square):
        if self.board.check_square(target_square)[0] == piece_color:
            return True
        return False

    @staticmethod
    def is_piece_on_board(self, piece_color, piece_type, current_square):
        if self.board.check_square(current_square) == (piece_color + piece_type):
            return True
        return False
    
    @staticmethod
    def is_capture(self, piece_color, target_square):
        if self.board.check_square(target_square)[0] == 'B' and piece_color == 'W' or\
           self.board.check_square(target_square)[0] == 'W' and piece_color == 'B':
            return True
        return False

    @staticmethod
    def is_piece_obstructed(self, current_square, target_square):
        vector = target_square - current_square
        if abs(vector[0]) == abs(vector[1]): 
            for i in range(1,abs(vector[0])):
                check = current_square + i*(vector/abs(vector[0]))
                if self.board.check_square(check) != '__':
                    return True
        if abs(vector[0]) != 0:
            for i in range(1,abs(vector[0])):
                check = current_square + i*(vector/abs(vector[0]))
                if self.board.check_square(check) != '__':
                    return True
        if abs(vector[1]) != 0:
            for i in range(1,abs(vector[1])):
                check = current_square + i*(vector/abs(vector[1]))
                if self.board.check_square(check) != '__':
                    return True

    @staticmethod
    def is_legal():
        return True #not coded yet
