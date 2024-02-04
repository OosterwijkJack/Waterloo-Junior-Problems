"""
name: Square pool

Iterate position of each tree (square can go down left, down right,up left,up right)

check every position surrounding the tree for square (8 positions)

create square array that keeps on expanding until meeting a wall or a tree

find array with the biggest size

this should not cause memory errors assuming max amount of trees is 100 as bruteforce works with graph size of 100x100 (5.5 seconds)
"""
import time
TREE = "🌲"
EMPTY = "🔳"
class Graph:
    def __init__(self, size, trees) -> None:
        self.size = size
        self.trees = trees

    def __str__(self) -> str:
        out = ""

        for i in self.data:
            for a in i:
                out += a
            out += "\n"

        return out
    
    def create_square_array(self, pos, direction, trees):
        # assume expanding right down

        size = 0
        while True:
            array = []
            size += 1
            for i in range(size):

                if size + self.pos[0] > self.size or size + self.pos[1] > self.size: # make sure array dosent leave the map
                    return size-1
                
                if self.is_tree(array): # check if tree in array
                    return size - 1
                
                array.append([(self.pos[0]+i, self.pos[1]+x) for x in range(self.size - (self.size - self.pos[1]))]) # contains positions square will be inside

    def is_tree(self,check): # check if array collides with tree
        for i in check:
            for a in i:
                if [a[0], a[1]] in self.trees:
                    return False
        return True
                
                
    
class Pos:
    def __init__(self,pos) -> None:
        self.pos = pos


    def moveR(self):
        self.pos = (self.pos[0], self.pos[1]+1)

    def moveD(self):
        self.pos = (self.pos[0]+1, self.pos[1])

    def resetL(self):
        self.pos = (self.pos[0],0)

    def get_pos(self):
        return self.pos


def main():
    size = int(input()) # size of square graph
    tree_num = int(input())
    trees = []
    for i in range(tree_num):
        a = str(input()).split()
        trees.append((int(a[0]),int(a[1])))

    start = time.time()

    graph = Graph(size, trees)

    print(time.time() - start)


def find_best_tree(trees,size):
    pass


main()