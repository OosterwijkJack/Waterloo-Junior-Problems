"""
Name: Bananas (Monkey Language)

Find out if a string is monkey language or not

1. A monkey language word is a special type of word called an A-word, which may be optionally
followed by the letter N and a monkey language word.
2. An A-word is either only the single letter A, or the letter B followed by a monkey language
word followed by the letter S

ANANA: monkey laungage because AN->monkey(AN)->monkey(A)

"""

def main():
    # if letter is A true
    # if letter is B check if monkey language word follows then has an S afterwards
    print(is_monkey_language("BBSANBASSNA"))

def is_monkey_language(word):
    N_index = 0
    if "N" in word:
        N_index = word.find("N")
        if not is_A_word(word[0:N_index], word): # a word before N
            return False
        if not is_monkey_language(word[N_index+1:]): # is monkey after the N
            return False
    else:
        if(not is_A_word(word, word)):
            return False
    return True
            

def is_A_word(text):

    if text == "A":
        return True
    
    if len(text) > 1:
        if text[0] == "B":

            if not is_monkey_language(text[1:-1]):
                return False
            if text[-1] != "S":
                return False
            
        else:
            return False
        
        return True
    



if __name__ == "__main__":
    main()