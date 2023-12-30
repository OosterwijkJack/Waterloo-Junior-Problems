"""
Name: Cross Spiral

The purpose of the program is to calculate the tile Bridget will be standing on given she walks a certain amount of steps
in a spiral within a cross within a room which dimensions are specified 

(first element is index of 1)
"""
import os
import time

class myArray:
    def __init__(self, data) -> None:
        self.data = data
        self.cur_pos = ()

    def __str__(self) -> str:
        out = ""
        for i in self.data:
            for a in i:
                out += a
            out += "\n"
        return out
    
    def get_pos(self): # returns current position
        return self.cur_pos
    def get(self): # return array
        return self.data
    
    def set_pos(self, pos): # sets position
        self.cur_pos = pos
    def walked_tile(self): # saves walked on tiles
        self.data[self.cur_pos[0]][self.cur_pos[1]] = "-"

    def next_pos(self, dir): # move to the next position depending on the direction
        self.walked_tile()
        if dir == "R":
            self.move_R()
        elif dir == "L":
            self.move_L()
        elif dir == "U":
            self.move_U()
        elif dir == "D":
            self.move_D()

    def get_value_L(self): # get values to left of position
        try:
            return self.data[self.cur_pos[0]][self.cur_pos[1]-1]
        except IndexError:
            return "."
    def get_value_R(self): # to right of
        try:
            return self.data[self.cur_pos[0]][self.cur_pos[1]+1]
        except IndexError:
            return "."
    def get_value_U(self): # above
        try:
            return self.data[self.cur_pos[0]-1][self.cur_pos[1]]
        except IndexError:
            return "."
    def get_value_D(self): # below
        try:
            return self.data[self.cur_pos[0]+1][self.cur_pos[1]]
        except IndexError:
            return "."
        # move depending on directions
    def move_R(self):
        self.cur_pos = (self.cur_pos[0], self.cur_pos[1]+1)
    def move_L(self):
        self.cur_pos = (self.cur_pos[0], self.cur_pos[1]-1)
    def move_U(self):
        self.cur_pos = (self.cur_pos[0]-1, self.cur_pos[1])
    def move_D(self):
        self.cur_pos = (self.cur_pos[0]+1, self.cur_pos[1])


def main():
    cur_dir = os.getcwd()
    data_index = 1 # which test data fild is used

    datain = open(f"/home/jack/Desktop/code/Waterloo-Junior-Problems/2005/Problem 4/testing/j4.{data_index}.in", "r").read().splitlines() # in data
    dataout = open(f"/home/jack/Desktop/code/Waterloo-Junior-Problems/2005/Problem 4/testing/j4.{data_index}.out", "r").read().splitlines() # in data 
    out = [] # program output

    outline_rect_dimensions = (int(datain[0]), int(datain[1]))
    cross_rect_dimensions = (int(datain[2]), int(datain[3]))
    steps = int(datain[4])

    rect = create_rect(outline_rect_dimensions, cross_rect_dimensions) # rect object making it easy to work with
    answer = (spiral(rect, steps))
    if testing(dataout, answer): # check if program output is correct
        print(answer)

def testing(dataout, out):
    # compare correct outputs and program output
    ok = None
    for a,i in zip(dataout, out):
        a = str(a)
        i = str(i)
        if a == i:
            print(":) good")
            ok = True
        else:
            print(":( Bad")
            print(f"correct output: {a}")
            print(f"your output: {i}")
            ok = False
    return ok

def spiral(rect: myArray, steps: int):
    dir_list = ["R","D","R","D","L","D","L","U","L","U","R","U"] # the direction needed to traverse a room shaped like a cross

    # T = Change direction when possible 
    # F = change direction when current direction is no longer possible
    meth_list = ["F", "T", "F", "F", "T", "F", "F", "T", "F", "F", "T","F"] 

    cur_dir_index = 0
    next_dir_index = 1
    rect.set_pos((0,rect.get()[0].index("A"))) # set pos to closest valid pos in first column
    
    for i in range(steps):
        # restart index when it exceeds number of direction changes list
        if cur_dir_index >= len(dir_list): 
            cur_dir_index = 0
        if next_dir_index >= len(dir_list):
            next_dir_index = 0

        cur_dir = dir_list[cur_dir_index]
        next_dir = dir_list[next_dir_index]

        if meth_list[cur_dir_index] == "T": # if method is change dir when possible
            if get_next_pos(next_dir, rect) == "A": # if next directin pos is possible
               rect.next_pos(next_dir) # move in direction
               cur_dir_index += 1 # next direction
               next_dir_index += 1
            else:
               rect.next_pos(cur_dir) # keep moving in same direction if else

        elif meth_list[cur_dir_index] == "F": # if method is change dir when current dir is no longer possible
            if get_next_pos(cur_dir, rect) == "A": # if cur dir is possible
                rect.next_pos(cur_dir) # keep going
            else:
                rect.next_pos(next_dir) # if not change to next direction
                cur_dir_index += 1
                next_dir_index += 1

    final_pos = rect.get_pos()
    final_pos = (final_pos[1]+1, final_pos[0]+1) # add one since problem wanted the first tile to be (1,1)
    return final_pos


# move in the direction of given direction
def next_pos(direction, rect: myArray):
    rect.walked_tile()
    if direction == "R":
        rect.move_R()
    elif direction == "L":
        rect.move_L()
    elif direction == "U":
        rect.move_U()
    elif direction == "D":
        rect.move_D()

# get position of next given direction
def get_next_pos(dir, rect: myArray):
    if dir == "R":
        return rect.get_value_R()
    elif dir == "L":
        return rect.get_value_L()
    elif dir == "U":
        return rect.get_value_U()
    elif dir == "D":
        return rect.get_value_D()

# create thje map
def create_rect(outline, cross):
    rect = [["A" for x in range(outline[0])]for y in range(outline[1])]# create array for rect
    for x in range(cross[0]):
        for y in range(cross[1]):
            rect[y][x] = "." # top left cutout in rect
            rect[y][x+outline[0]-cross[0]] = "." # top right cutout in rect

            rect[y + outline[1]-cross[1]][x] = "." # bottom left cutout in rect
            rect[y+outline[1]-cross[1]][x+outline[0]-cross[0]] = "." # bottom right cutout in rect
    return myArray(rect) # array object



if __name__ == "__main__":
    main()