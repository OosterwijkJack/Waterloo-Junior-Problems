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

def main():
    # if letter is A true
    # if letter is B check if monkey language word follows then has an S afterwards
    pass




if __name__ == "__main__":
    main() 