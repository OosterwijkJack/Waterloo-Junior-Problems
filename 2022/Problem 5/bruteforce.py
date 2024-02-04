"""
name: Square pool

make graph represent trees as . 
iterate graph and start making bigger and bigger square until tree is touched
log size of squarer
return biggest square

This solution to the problem is not a true soluction as it times out in big quantities

brute force time = graph_size^2
tree check time = trees*32

max trees = 100
max graph_size = 500 000
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
    
    def search_sqaure(self,pos):
        size = 0
        while True:
            area = []
            size += 1
            for i in range(size):
                try:

                    if pos[0] + i > len(self.data) or pos[1] + size > len(self.data[0]): # make sure index is in range
                        raise IndexError
                    
                    area.append(self.data[pos[0] + (i)][pos[1]:pos[1]+size])
                except IndexError:
                    return size -1
                
            for i in area:
                for a in i:
                    if a == TREE:
                        return size -1
        

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
    graph = create_graph(size,trees) # create the graph 
    print(graph) # show pretty graph
    size = iter_graph(graph) # iter
    print(size)  # out

    print(time.time() - start)


def iter_graph(graph): # iterates each position in graph and finds largest square
    big_size = 0 # biggest size
    pos = Pos((0,0))

    for i in graph.data:

        for a in i:

            search_size = graph.search_sqaure(pos.get_pos()) # finds size of biggest square in pos
            if search_size > big_size: # if its the new big assign 
                print(pos.get_pos(), search_size)
                big_size = search_size

            pos.moveR()
        pos.moveD()
        pos.resetL()

    return big_size

def create_graph(size, trees): # create graph object with graph data
    graph = [[EMPTY for x in range(size)] for y in range(size)]

    for i in trees:
        graph[i[0]-1][i[1]-1] = TREE
    
    graph = Graph(graph)
    return graph
    

main()