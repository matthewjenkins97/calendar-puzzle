import numpy as np

# gameboard_for_live_example = [
#     [' ',' ',' ',' ',' ',' ','X'],
#     [' ',' ',' ',' ',' ',' ','X'],
#     [' ',' ',' ',' ',' ',' ',' '],
#     [' ',' ',' ',' ',' ',' ',' '],
#     [' ',' ',' ',' ',' ',' ',' '],
#     [' ',' ',' ',' ',' ',' ',' '],
#     [' ',' ',' ','X','X','X','X']]

# pieces for live example:
# [['A','A'],
#  ['A',' '],
#  ['A','A']], 

# [[' ','B','B'],
#  [' ','B',' '],
#  ['B','B',' ']]

# [[' ','C'],
#  ['C','C'],
#  [' ','C'],
#  [' ','C']]

# [[' ','D'],
#  ['D','D'],
#  ['D','D']], 

# [['E','E'],
#  ['E','E'],
#  ['E','E']], 

# [['F','F'],
#  [' ','F'],
#  [' ','F'],
#  [' ','F']]

# [[' ','G'],
#  [' ','G'],
#  ['G','G'],
#  ['G',' ']]

# [['H',' ',' '],
#  ['H',' ',' '],
#  ['H','H','H']]

class GameBoard:
    gameboard = [[]]
    placed_pieces = []

    def __init__(self, default_gameboard):
        self.gameboard = default_gameboard

    def place_piece(self, piece, x, y):
        

        placed_pieces.append(piece)


class Piece:
    shape = [[]]
    rotation = ' ' # will be N, E, S, or W
    front_or_back = ' ' # will be F or B (could be a boolean if necessary)
    placed = False

    def __init__(self, default_shape, default_rotation, default_front_or_back):
        self.shape = default_shape
        self.rotation = default_rotation
        self.front_or_back = default_front_or_back

    def rotate_clockwise(self):
        self.shape = np.rot90(self.shape, k=1, axes=(1,0))

        match self.rotation:
            case 'N':
                self.rotation = 'E'
            case 'E':
                self.rotation = 'S'
            case 'S':
                self.rotation = 'W'
            case 'W':
                self.rotation = 'N'
            case _:
                raise Exception()

    def rotate_counterclockwise(self):
        self.shape = np.rot90(self.shape, k=1)

        match self.rotation:
            case 'N':
                self.rotation = 'W'
            case 'E':
                self.rotation = 'N'
            case 'S':
                self.rotation = 'E'
            case 'W':
                self.rotation = 'S'
            case _:
                raise Exception()
    
    def flip(self):
        self.shape = np.flip(self.shape)

        match self.front_or_back:
            case 'F':
                self.front_or_back = 'B'
            case 'B':
                self.front_or_back = 'F'
            case _:
                raise Exception()

    def __str__(self):
        shape_string = ''
        for row in self.shape:
            for col in row:
                shape_string += col
            shape_string += '\n'
        return f'{shape_string}\nRotation: {self.rotation}\nFront or Back: {self.front_or_back}\n'

def main():
    piece = Piece([ ['X','X'],
                    [' ','X'],
                    [' ','X'],
                    [' ','X']], 'N', 'F')

main()