
"""
MENU
5
7
F T R U B L K
P M N A X C U
A E R C N E O
M N E U A R M
M U N E M N S

"""
class Menu:
    def __init__(self,data) -> None:
        self.data = data
        self.pos = ()
    def __str__(self) -> str:
        out = ""
        for i in self.data:
            for a in i:
                out += a + " "
            out += "\n"
        return out

def main():
    word = str(input())
    dimensions = (int(input()), int(input()))
    letters = []

    for i in range(dimensions[0]):
        letters.append(str(input()).replace(' ', ''))
        
    menu = Menu(letters)
    print("\n")
    print(menu)
if __name__ == "__main__":
    main()