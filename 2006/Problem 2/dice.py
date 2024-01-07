"""
Name: Roll the Dice

This program outputs the the total amount of ways the number 10 can be rolled
on 2 dice given the amount of sides the dice gave assuming the sides range from
1-number of sides

"""

def main():
    d1 = int(input("Enter m: "))
    d2 = int(input("Enter n: "))

    print(begin(d1,d2))

def begin(*data):
    combinations = (get_total_combinations(data[0],data[1]))
    return f"There are {combinations} ways to form the sum 10." if combinations != 1 else \
    f"There is {combinations} way to form the sum 10."

def get_total_combinations(d1,d2): # return total combinations of sides that equal to 10
    # number more than 10 becomes 10 
    d1 = min(d1, 10) 
    d2 = min(d2, 10)

    print(d1,d2)

    combinations = 0
    # check all combinations
    for i in range(d1):
        for a in range(d2):
            if i+1 + a+1 == 10:
                combinations += 1
    return combinations

if __name__ == "__main__":
    main()