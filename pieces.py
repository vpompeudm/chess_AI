import numpy as np

class Pieces():

    def __init__(self):
        pass

    def is_valid_piece_move(self, piece_color, piece_type, current_square, target_square, is_capture):
        if piece_type == 'N':
            return self.move_knight(current_square, target_square)

        if piece_type == 'R':
            return self.move_rook(current_square, target_square)
            
        if piece_type == 'B':
            return self.move_bishop(current_square, target_square)
                
        if piece_type == 'Q':
            return self.move_queen(current_square, target_square)
            
        if piece_type == 'K':
            return self.move_king(current_square, target_square)
        
        if piece_type == 'P':
            return self.move_pawn(piece_color, current_square, target_square, is_capture)
        
        return False

    @staticmethod    
    def move_knight(current_square, target_square):

        if (abs(target_square[0] - current_square[0]) == 2 and abs(target_square[1] - current_square[1]) == 1) or\
           (abs(target_square[0] - current_square[0]) == 1 and abs(target_square[1] - current_square[1]) == 2):
            return True
        return False

    @staticmethod
    def move_rook(current_square, target_square):
        if (current_square[0] == target_square[0] and current_square[1] != target_square[1]) or \
           (current_square[0] != target_square[0] and current_square[1] == target_square[1]):
            return True
        return False

    @staticmethod
    def move_bishop(current_square, target_square):
        if abs(target_square[0]-current_square[0]) ==  abs(target_square[1]-current_square[1]):
            return True
        return False
    
    @staticmethod
    def move_queen(current_square, target_square):
        if (current_square[0] == target_square[0] and current_square[1] != target_square[1]) or \
           (current_square[0] != target_square[0] and current_square[1] == target_square[1]) or \
           (abs(target_square[0]-current_square[0]) == abs(target_square[1]-current_square[1])):
            return True
        return False
    
    @staticmethod
    def move_king(current_square, target_square):
        vector = target_square - current_square

        if all(np.abs(vector)) in [0,1]:
            return True
        return False
    
    @staticmethod
    def move_pawn(piece_color, current_square, target_square, is_capture):
        if piece_color == 'W':
            if (target_square[1] == current_square[1]+1 and target_square[0] == current_square[0]) or\
               (target_square[1] == current_square[1]+2 and current_square[1] == 1) or\
               (target_square[1] == current_square[1]+1 and abs(target_square[0] - current_square[0]) == 1 and is_capture):
               return True
        if piece_color == 'B':
            if (target_square[1] == current_square[1]-1 and target_square[0] == current_square[0]) or\
               (target_square[1] == current_square[1]-2 and current_square[1] == 6) or\
               (target_square[1] == current_square[1]-1 and abs(target_square[0] - current_square[0]) == 1 and is_capture):
               return True
        return False 