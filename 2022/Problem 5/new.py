"""
name: Square pool

Iterate position of each tree (square can go down left, down right,up left,up right)

create square array that keeps on expanding until meeting a wall or a tree

find array with the biggest size

this should not cause memory errors assuming max amount of trees is 100 as bruteforce works with graph size of 100x100 (5.5 seconds)
"""
import time
TREE = "🌲"
EMPTY = "🔳"
class Graph:
    def __init__(self,data) -> None:
        self.data = data

    def __str__(self) -> str:
        out = ""

        for i in self.data:
            for a in i:
                out += a
            out += "\n"

        return out
    
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



    print(time.time() - start)


def find_best_tree(trees,size):
    pass


main()