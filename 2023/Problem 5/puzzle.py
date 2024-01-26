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

    def __init__(self, data, word) -> None:
        self.data = data
        self.word = word

    def __str__(self) -> str:
        out = ""
        for i in self.data:
            for a in i:
                out += a
                out += " "
            out += "\n"
        return out
    
    # straight
    def get_U(self, pos):
        try:
            not_negative(pos[0]-1)
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
            not_negative(pos[1]-1)
            return self.data[pos[0]][pos[1]-1]
        except IndexError:
            return 0
    def get_R(self, pos):
        try:
            return self.data[pos[0]][pos[1]+1]
        except IndexError:
            return 0
    # diagonal   
    def get_RU(self, pos):
        try:
            not_negative(pos[0]-1)
            return self.data[pos[0]-1][pos[1] + 1]
        except IndexError:
            return 0
    def get_RD(self, pos):
        try:
            return self.data[pos[0]+1][pos[1]+1]
        except IndexError:
            return 0
        
    def get_LU(self, pos):
        try:
            not_negative(pos[0]-1)
            not_negative(pos[1]-1)
            return self.data[pos[0]-1][pos[1]-1]
        except IndexError:
            return 0
    def get_LD(self, pos):
        try:
            not_negative(pos[1]-1)
            return self.data[pos[0]+1][pos[1]-1]
        except IndexError:
            return 0
            
    def get_all_diretions(self, pos):
        
        return [
            (self.get_L(pos),"L"),
            (self.get_R(pos),"R"),
            (self.get_U(pos),"U"),
            (self.get_D(pos),"D"),
            (self.get_LU(pos),"LU"),
            (self.get_LD(pos),"LD"),
            (self.get_RU(pos),"RU"),
            (self.get_RD(pos),"RD")
        ]

class Pos:
    def __init__(self, pos) -> None:
        self.pos = pos
    #straight
    def mov_R(self):
        self.pos = (self.pos[0], self.pos[1]+1)
    def mov_L(self):
        self.pos = (self.pos[0], self.pos[1]-1)
    def mov_U(self):
        self.pos = (self.pos[0]-1, self.pos[1])
    def mov_D(self):
        self.pos = (self.pos[0]+1, self.pos[1])

    # diagonal
    def mov_RU(self):
        self.pos =  (self.pos[0]-1, self.pos[1] + 1)
    def mov_RD(self):
        self.pos =  (self.pos[0]+1, self.pos[1] + 1) 
    def mov_LU(self):
        self.pos =  (self.pos[0]-1, self.pos[1] - 1)
    def mov_LD(self):
        self.pos =  (self.pos[0]+1, self.pos[1] - 1)

    def reset_L(self):
        self.pos = (self.pos[0], 0)   

    def get(self):
        return self.pos

def main():
    word = "MENU"
    dimensions = (5, 7)
    wrd_map = """F T R U B L K
P M N A X C U
A E R C N E O
M N E U A R M
M U N E M N S""".split("\n")
    wrd_map = WordMap([x.replace(" ", "") for x in wrd_map], word)

    print()
    print(wrd_map)

    print(iterate_word_map(wrd_map))

def iterate_word_map(wrd_map):
    pos = Pos((0,0))
    instances = 0

    for i in wrd_map.data:
        for a in i:
            if a == wrd_map.word[0]:
                valid_directions = get_valid_direction(wrd_map, pos)
                instances += [search_direction(wrd_map, pos, x) for x in valid_directions].count(True)
            pos.mov_R() # move right

        pos.mov_D() # move down
        pos.reset_L() # move to beggining of list 
    return instances


def search_direction(wrd_map:WordMap, pos:Pos, direction): # takes direction and contiously searches for next word
    new_pos = Pos(pos.get())
    all_letters = wrd_map.word[0]
    # direction is a tuple containing the path and what direction the path is going
    for i in range(1,len(wrd_map.word)):

        letter = get_next_letter(wrd_map, new_pos, direction[1]) # next letter in dir

        if letter:
            all_letters += letter # all letters found adds up
        
        if all_letters == wrd_map.word:
            return True
        
        if letter != wrd_map.word[i]:
            return False
    return True

# gets next letter depending on position and direction
def get_next_letter(wrd_map:WordMap, pos:Pos,direction):
    if direction == "R":
        next = wrd_map.get_R(pos.get())
        pos.mov_R()
        return next
    if direction == "L":
        next = wrd_map.get_L(pos.get())
        pos.mov_L()
        return next
    if direction == "U":
        next = wrd_map.get_U(pos.get())
        pos.mov_U()
        return next
    if direction == "D":
        next = wrd_map.get_D(pos.get())
        pos.mov_D()
        return next
    if direction == "RU":
        next = wrd_map.get_RU(pos.get())
        pos.mov_RU()
        return next
    if direction == "RD":
        next = wrd_map.get_RD(pos.get())
        pos.mov_RD()
        return next
    if direction == "LU":
        next = wrd_map.get_LU(pos.get())
        pos.mov_LU()
        return next
    if direction == "LD":
        next = wrd_map.get_LD(pos.get())
        pos.mov_LD()
        return next
    
# return directions which next letter is the same as first letter of word
def get_valid_direction(wrd_map:WordMap, pos: Pos):
    directions = wrd_map.get_all_diretions(pos.get())
    valid = []

    for i in directions:
        if i[0] == wrd_map.word[1]: # second letter in word since this is where the search starts
            valid.append(i)
    return valid

def not_negative(value):
    if value <0:
        raise IndexError
        
if __name__ == "__main__":
    main()


    