"""
Plan:
Iterate through each letter in list

check all valid directions for the following letter

if following letter exists in valid direction repeat 

(if letter found and there was also another possible route of the word jump back to beginning of two possible letters.)

if  not jump to orignal letter in iteration and check next direction

if all directions checked jump to next letter in iteration


words can be found if letters are at a 90 degree angle but only once per branch


p
e
r h a p s
h
a 
p 
s  

example of perhaps occuring in a word hunt twice
"""
class WordMap:

    def __init__(self, a,b) -> None:
        self.data = (a,b)

    def __str__(self) -> str:
        out = ""
        for i in self.data:
            for a in i:
                out += a
                out += " "
            out += "\n"
        return out
    
    def get_U(self, pos):
        try:
            return self.data[pos[0]-1][pos[1]]
        except IndexError:
            return 0
    def get_D(self, pos):
        try:
            return self.data[pos[0]+1][pos[1]]
        except IndexError:
            return 0
    def get_L(self, pos):
        try:
            return self.data[pos[0]][pos[1]-1]
        except IndexError:
            return 0
    def get_R(self, pos):
        try:
            return self.data[pos[0]-1][pos[1]+1]
        except IndexError:
            return 0

class Pos:
    def __init__(self, pos) -> None:
        self.pos = pos
    
    def mov_R(self):
        self.pos = (self.pos[0], self.pos[1]+1)
    def mov_L(self):
        self.pos = (self.pos[0], self.pos[1]-1)
    def mov_U(self):
        self.pos = (self.pos[0]-1, self.pos[1])
    def mov_D(self):
        self.pos = (self.pos[0]+1, self.pos[1])
    def reset_L(self):
        self.pos = (self.pos[0], 0)   

def main():
    word = str(input())
    dimensions = (int(input()), int(input()))
    wrd_map = WordMap([input().replace(" ", "") for _ in range(dimensions[0])])

    print()
    print(wrd_map)

def iterate_word_map(wrd_map):
    pos = Pos(0,0)

    for i in wrd_map:
        for a in i:


            pos.mov_R() # move right

        pos.mov_D() # move down
        pos.reset_L() # move to beggining of list 

if __name__ == "__main__":
    main()


    