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

WHITE = 1
BLACK = 0
color = bool(BLACK)

@ dataclass
class Vec2:
    x : int = 0
    y : int = 0

class Board:
    def __init__(self,data) -> None:
        self.data = data
        self.size = Vec2(8,8)
    
    def __str__(self): # display board
        out = ""
        for i in self.data:
            out += "".join([str(x) for x in i]) + "\n"
        return out
    
    def get(self, pos: Vec2): # return value of tile and its position
        return (self.data[pos.x][pos.y], pos)
    def set(self,pos:Vec2, value):
        self.data[pos.x][pos.y] = value
    
    def count_checkers(self):
        black = 0
        white = 0
        for i in self.data:
            for a in i:
                if a == WHITE_CIRCLE:
                    white += 1
                elif a == BLACK_CIRCLE:
                    black += 1
        return [black,white]

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
    print(begin("c 4 8 7 8 2 4 7 8 8"))
    #global color

    #scene = create_board()
    #scene.set_config_A()
    #print(scene)
    #pos = Vec2(5-1,6-1)

    #moves = (valid_moves(scene, pos))
    #make_moves(scene, moves, pos)

def begin(user_input:str):
    global color
    user_input = user_input.split()
    scene = create_board()

    match user_input[0]:
        case 'a':
            scene.set_config_A()
        case 'b':
            scene.set_config_B()
        case 'c':
            scene.set_config_C()
    if len(user_input) > 2:
        user_moves = [Vec2(int(user_input[x])-1,int(user_input[x+1])-1) for x in range(2,len(user_input),2)]
    else: user_moves = []

    for i in user_moves:
        pos = i
        moves = valid_moves(scene, pos)
        make_moves(scene,moves,pos)
        color = not color
        print(scene)

    return scene.count_checkers()

def make_moves(scene:Board, moves:list, pos: Vec2):
    current = BLACK_CIRCLE if color == BLACK else WHITE_CIRCLE
    if len(moves)> 0:
        scene.set(pos, current)
    for i in moves:
        for a in range(len(i)) :
            scene.set(i[a][1], current)  

def is_checkers(scan):
    values = []
    for i in scan:
        values += i[0]
    return BLACK_CIRCLE in values and WHITE_CIRCLE in values

def valid_moves(scene: Board, pos: Vec2): # decides wether the position of a move is valid
    scan = scan_board(scene, pos)
    scan = list(filter(is_checkers,scan)) # remove scans that dont have both color checkers
    opposite = BLACK_CIRCLE if color == WHITE else WHITE_CIRCLE # store opposite checker than current 
    current = BLACK_CIRCLE if color == BLACK else WHITE_CIRCLE

    opp_passed = False # wether the move passes a non-flipped checker in a line
    moves = []
    for i in (scan):
        for a in range(len(i)):
            if i[a][0] != opposite: # must start with opposite piece
                if a == 0:
                    break

            if i[a][0] == current:
                if a != 0:
                    moves.append(i[:a+1])
                    break

    return moves


def scan_board(scene: Board, pos: Vec2): # returns a list of all pieces on board from every direction starting at a position
    straight_scan = scan_straight(scene,pos)
    diagonal_scan = scan_diagonal(scene,pos)

    return straight_scan + diagonal_scan

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