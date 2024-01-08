"""
Name: Chell-Phone Messaging

Calculate how much time is needed to type certain words on phone assuming one word requires 
one second and a pause requires 2

"""

letter_num_list = [
    ["a", "b", "c"],
    ['d','e','f'],
    ['g','h','i'],
    ['j','k','l'],
    ['m','n','o'],
    ['p','q','r','s'],
    ['t','u','v'],
    ['w','x','y','z']
]

def main():
    user_input = []
    while True: # get user input until hault
        a = input()
        if a == "halt": break
        user_input.append(a)

    print("\n".join(begin(*user_input))) # print data

# begin program with user input
def begin(*data):

    out = []
    for i in data:
        word_as_num = word_to_number(i) # word to numbers and pauses
        out.append(number_to_time(word_as_num)) # out append sequence converted to time 
        if i == "halt": break
    return out
    

# converts a word to numbers on a phone and pauses
def word_to_number(word):
    out = []
    for i in word:
        button = letter_to_button(i)

        if len(out) > 0:
            if out[-1][0] == button[0]:
                out.append("pause")

        out.append(button)
    return out

# converts numbers on phone and pauses to time
def number_to_time(number: list):
    total_time = 0

    for i in number:
        if i == "pause":
            total_time += 2
            continue
        total_time += len(i)
    return str(total_time)

# converts letter to button clicks on phone
def letter_to_button(letter):
    for a,i in enumerate(letter_num_list):
        if letter in i: # if letter in button
            index = letter_num_list.index(letter_num_list[a]) + 2 # index of letter + 2 since letters start on button 2
            return str(index) + (str(index) * letter_num_list[a].index(letter))
if __name__ == "__main__":
    main()