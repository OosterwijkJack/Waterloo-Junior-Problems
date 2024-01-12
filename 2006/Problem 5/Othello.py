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

"""
BLACK_SQUARE = "⬛"
WHITE_SQUARE = "⬜"

BLACK_CIRCLE = "⚫"
WHITE_CIRCLE = "⚪"

@ dataclass
class Vec2:
    x : int = 0
    y : int = 0

class Board:
    def __init__(self,data) -> None:
        self.data = data
    
    def __str__(self): # display board
        out = ""
        for i in self.data:
            out += "".join([str(x) for x in i]) + "\n"
        return out
    
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
    scene.set_config_C()
    print(scene)

def begin(data):
    pass

def create_board():
    return Board([[BLACK_SQUARE if x % 2 ==0 else WHITE_SQUARE for x in range(8)] for y in range(8)])

if __name__ == "__main__":
    main()