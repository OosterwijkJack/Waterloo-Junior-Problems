"""
Name: Its tough being a teen

This  program creates instructions of tasks which have to be completed before other tasks
in a set of tasks

task is 1-7

Your “to do” list (above) can now be abbreviated to:
1,7 -> task 1 before 7
1,4 -> task 1 before 4
2,1 -> so on
3,4
3,5

Sample Input 1
6
2
5
4
0
0
Output for Sample Input 1
3 5 6 2 1 4 7

Explanation for Sample Output 1

The input data tells us that task 6 must be performed before task 2, and task 5 before task 4. The
only tasks with no prerequisites are 3 and 6, so we choose 3 because it has the lower number. Then
5 and 6 are possible; 5 is chosen, then 6. Next must come 2, followed by 1. Then both 4 and 7 are
possible; the lower one is chosen first

"""
import itertools
def main():
    datain = []

    while True:
        first = int(input())
        second = int(input())

        datain.append(first) 
        datain.append(second)

        if first == 0 and second == 0:
            break

    print(begin(datain))

def begin(data:list):
    a = [[1,7], [1,4], [2,1], [3,4], [3,5]] # original instructions

    # new "Emailed instructions"
    if len(data) == 2:
        data = []
    else:
        data = data[:-2]
        
    data = [data[i:i+2] for i in range(0, len(data), 2)] # convert to lists in list containing first 2 elements
    data = a + data # merge two lists

    # returns list of every possible unique list 
    all_combos = list(itertools.permutations(range(1,8), 7)) # unique number 1-7 7 times

    correct_list = []
    for i in all_combos: # loop every possible list
        if valid_list(data, i): # if list valid
            correct_list = i # assign
            break

    if correct_list: 
        return [" ".join([str(x) for x in correct_list])]
    else:
        return ["Cannot complete these tasks.  Going to bed."]
 

def valid_list(sort, data: list):
    # loop instructions
    for a in sort:
        try:
            if data.index(a[0]) > data.index(a[1]): # if instructions are not present in list
                return False
        except:
            return False
    return True 


if __name__ == "__main__":
    main()