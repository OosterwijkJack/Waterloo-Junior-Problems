from dataclasses import dataclass

"""
Name: CCC Othello


Program simulates game of Otello

Othello is a game on 8x8 checker grid. Game will have 3 starting prefixes. 
Black goes first then white then black and so on

A piece must be placed adjacent to another piece (i.e, beside a piece either horizontally, vertically or diagonally).

At least one of your opponents' discs must be “flipped.” (meaning changing the color of the disk) If you are playing black pieces, you
flip your opponents' (white) pieces (to black) so long as your opponents' pieces are on a line
(either horizontally, vertically or diagonally) between the latest piece placed on the board
and another black piece, with no other black pieces or empty squares in between the most
recently placed black piece and the given white piece. The same rule applies if the player is
placing white pieces.



program the get input for: amount of turns (0-30), then followed by where the pieces will be placed on the board (row, column) (1-8)

program outputs amount of white pieces on board followed by amount of black pieces

1. do a scan of all directions including diagnoal
1.1 left, right, up, down, diagnol left, diagonal right
1.2 two functions one for straight and one for diagonal
2. return directions in a list containing each step in path when move is valid
3. write to board the move

"""
BLACK_SQUARE = "⬛"
WHITE_SQUARE = "⬜"

BLACK_CIRCLE = "⚫"
WHITE_CIRCLE = "⚪"

@ dataclass
class Vec2:
    y : int = 0
    x : int = 0

@ dataclass
class Scan:
    left: list
    right: list
    up: list
    down: list

    diag_left_up: list
    diag_right_up: list
    diag_left_down: list
    diag_right_down: list

class Board:
    def __init__(self,data) -> None:
        self.data = data
        self.size = Vec2(8,8)
    
    def __str__(self): # display board
        out = ""
        for i in self.data:
            out += "".join([str(x) for x in i]) + "\n"
        return out
    
    def get(self, pos: Vec2): # return value of tile
        return self.data[pos.x][pos.y]
    
    def set_tile_black(self, pos:Vec2): # places black checker on given tile
        self.data[pos.x][pos.y] = BLACK_CIRCLE
    def set_tile_white(self, pos:Vec2):# places white checker on given tile
        self.data[pos.x][pos.y] = BLACK_CIRCLE

    def set_config_A(self): # 4 white and black checkers in middle
        self.data[3][3] = WHITE_CIRCLE
        self.data[3][4] = BLACK_CIRCLE

        self.data[4][3] = BLACK_CIRCLE
        self.data[4][4] = WHITE_CIRCLE

    def set_config_B(self): # creates an X of checkers
        for a,i in enumerate(self.data):
            i[a] = BLACK_CIRCLE
            i[len(self.data)-1-a] = WHITE_CIRCLE

    def set_config_C(self): # 2 black then 2 white checkers in middle all the way down to bottom of board
        for i in self.data:
            i[2:4] = [BLACK_CIRCLE,BLACK_CIRCLE]
            i[4:6] = [WHITE_CIRCLE,WHITE_CIRCLE]


def main():
    scene = create_board()
    scene.set_config_A()
    print(scene)

    scan = scan_board(scene, Vec2(3, 3))
    print(scan)


def scan_board(scene: Board, pos: Vec2): # returns a list of all pieces on board from every direction starting at a position
    straight_scan = scan_straight(scene,pos)
    diagonal_scan = scan_diagonal(scene,pos)

    data = straight_scan + diagonal_scan
    return Scan(*data)

def scan_straight(scene: Board, pos: Vec2):
    # left scan
    left_range = pos.x + 1
    data_L = []
    for i in range(1,left_range):
        next_pos = Vec2(pos.x - i, pos.y)
        data_L.append(scene.get(next_pos))   
    #right scan
    right_range = scene.size.x - pos.x # number of tiles to right of pos
    data_R = []
    for i in range(1,right_range):
        next_pos = Vec2(pos.x + i, pos.y)
        data_R.append(scene.get(next_pos))
    # up scan
    up_range = pos.y + 1
    data_U = []
    for i in range(1,up_range):
        next_pos = Vec2(pos.x, pos.y-i)
        data_U.append(scene.get(next_pos))
    # down scan
    down_range = scene.size.y - pos.y
    data_D = []
    for i in range(1,down_range):
        next_pos = Vec2(pos.x, pos.y+i)
        data_D.append(scene.get(next_pos))
    return [data_L, data_R, data_U, data_D]

def scan_diagonal(scene: Board,pos: Vec2):
    # left up scan
    left_range = min([pos.x+1, pos.y+1]) # find smallest value between left and up for diagonal
    data_LU = []
    for i in range(1,left_range):
        next_pos = Vec2(pos.x - i, pos.y -i)
        data_LU.append(scene.get(next_pos))   
    #right up scan
    right_range = min([scene.size.x - pos.x, pos.y+1]) 
    data_RU = []
    for i in range(1,right_range):
        next_pos = Vec2(pos.x + i, pos.y - i)
        data_RU.append(scene.get(next_pos))
    # left down scan
    up_range = min([pos.x+1,scene.size.y - pos.y ]) 
    data_LD = []
    for i in range(1,up_range):
        next_pos = Vec2(pos.x-i, pos.y+i)
        data_LD.append(scene.get(next_pos))
    # right down scan
    down_range = min([scene.size.x - pos.x,scene.size.y - pos.y])
    data_RD = []
    for i in range(1,down_range):
        next_pos = Vec2(pos.x+i, pos.y+i)
        data_RD.append(scene.get(next_pos))

    return [data_LU, data_RU, data_LD, data_RD]

def create_board(): # makes checker board of 8 by 8 dimensions
    row1 = [BLACK_SQUARE if x % 2 ==0 else WHITE_SQUARE for x in range(8)] 
    row2 = [WHITE_SQUARE if x % 2 ==0 else BLACK_SQUARE for x in range(8)]
    return Board([row1.copy() if x % 2 == 0 else row2.copy() for x in range(8)]) # if copy is not used all lists are the same and updated the same

if __name__ == "__main__":
    main()