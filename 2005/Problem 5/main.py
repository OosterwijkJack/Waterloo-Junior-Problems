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
    """
    data_index = 3
    cur_dir = os.getcwd()
    datain = open(os.path.join(cur_dir,f"testing/j5.{data_index}.in"),"r").read().splitlines() # in data
    dataout = open(os.path.join(cur_dir,f"testing/j5.{data_index}.out"),"r").read().splitlines() # in data 
    out = [] # program output
    
    for i in datain[0:-1]:
        try:
            if (is_string_valid(i)):
                out.append("YES")
            else:
                out.append("NO")
        except IndexError:
            out.append("YES")

    output = testing(dataout, out)
    if output:
        print('\n'.join(out))
    """
    
    try:
        if (is_string_valid("BBASNBASSNA")):
            print("YES")
        else:
            print("NO")
    except IndexError:
        print("YES")
        


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
    index = 0
    monkey_word = False

    while index < len(word)-1: # loop until every letter in entire word has been checked 
        # check if monkey word function returns the index you need to check
        # because there are money words in monkey words 
        monkey = is_monkey_word(word,index) 
        if monkey != FALSE:
            index = monkey+1 # update to index if string is so far valid
        else:
            return False
    return True

def is_A_word(word,index):
    no_call = True
    global unfinished_B
    if word[index] == "A": # If letter is A return index as it is a valid A word and needs no further steps
        return index
    
    if word[index] == "B":
        no_call = False
        unfinished_B += 1
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
        except IndexError: # reached end without finishing a B
            return FALSE
    else:
        return FALSE   # A word has to start with be A or B 
    
    if no_call: # when calls start to reverse index needs to stay
        return new_index
    else:
        return index # call is not reversing return normal index


def is_monkey_word(word,index):
    global unfinished_B
    no_call = True
    new_index = is_A_word(word,index) # monkey word always starts with A_word
    if new_index == FALSE: # does not start with a_word
        return FALSE
    
    if word[new_index] == "A":
        no_call = False
        index += 1

    try:
        if word[index] == "N":
            no_call = False
            index +=1
            new_index = is_monkey_word(word, index)
            if new_index != FALSE:
                return new_index
            else:
                return FALSE
    except IndexError:
        if (unfinished_B) > 0:
            return False
        else:
            raise IndexError
    if new_index == len(word)-1:
        return new_index
    else:
        if no_call:
            return new_index
        else:
            return index


if __name__ == "__main__":
    main() 