"""
Name: Bananas (Monkey Language)

Find out if a string is monkey language or not

1. A monkey language word is a special type of word called an A-word, which may be optionally
followed by the letter N and a monkey language word.
2. An A-word is either only the single letter A, or the letter B followed by a monkey language
word followed by the letter S


Create a diagram of how every possibility should be handled then program 
ANBASNBBASNAS -> monkey(A_word(A)) ->  N -> monkey(a_word(B)-> monkey(a_word(A))-> S) -> N
-> monkey(a_word(B) -> monkey(a_word(B) ->  monkey(a_word(A) -> S ) -> N -> monkey(a_word(A)) -> S) 



"""

import os
FALSE = -1
unfinished_B = 0
def main():
    data_index = 4
    cur_dir = os.getcwd()
    datain = open(os.path.join(cur_dir,f"2005/Problem 5/testing/j5.{data_index}.in"),"r").read().splitlines() # in data
    dataout = open(os.path.join(cur_dir,f"2005/Problem 5/testing/j5.{data_index}.out"),"r").read().splitlines() # in data 
    out = [] # program output
    
    for i in datain[0:-1]:
        try:
            if (is_string_valid(i)):
                out.append("YES")
            else:
                out.append("NO")
        except IndexError: # index error means reached end of string without any invalid words
            out.append("YES") # string is valid

    if testing(dataout, out):
        print("\n".join(out))
    
    
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

def is_string_valid(word):
    global unfinished_B
    index = 0
    unfinished_B = 0

    while index < len(word): # loop until every letter in entire word has been checked 
        # check if monkey word function returns valid index
        # because there are monkey words in monkey words so index is always changing
        monkey = is_monkey_word(word,index) 
        if monkey != FALSE:
            index = monkey+1 # update to index if string is so far valid
        else:
            return False
    return True

def is_A_word(word,index):
    global unfinished_B
    if word[index] == "A": # If letter is A return index + 1 as it is a valid A word and needs no further steps
        return index + 1
    
    if word[index] == "B": # letter is B
        unfinished_B += 1 # keep tracked of B's that have not been completed by an S
        index += 1 # increase index
        new_index = is_monkey_word(word, index) # following B has to be a monkey word
        if new_index != FALSE: # if is monkey word return index
            index = new_index 
        else:
            return FALSE # not monkey !
        
        try:
            if word[index] != "S": # B has to end with S
                return FALSE
            else:
                unfinished_B -= 1 # B finished
                index += 1
        except IndexError: # reached end without finishing a B
            return FALSE
    else:
        return FALSE   # A word has to start with be A or B 
       
    return index # return current index for next func

def is_monkey_word(word,index):
    global unfinished_B
    new_index = is_A_word(word,index) # monkey word always starts with A_word

    if new_index == FALSE: # does not start with a_word
        return FALSE # not monkey :(
    else:
        index = new_index # set index to new if index is valid

    try:
        if word[index] == "N": # if a_word is followed by N
            index +=1
            new_index = is_monkey_word(word, index) # must be followed by another monkey word
            if new_index != FALSE: # valid index
                index = new_index 
            else:
                return FALSE # not monkey
    except IndexError:
        if (unfinished_B) > 0: # if all B's are not finished
            return False # not monkey
        else:
            raise IndexError # this means we have reached end of list with no error. index error is handled elsewhere
    return index # return current index for next func


if __name__ == "__main__":
    main() 