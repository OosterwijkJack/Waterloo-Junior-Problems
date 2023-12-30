"""
Name: Returning home
Purpose of this program is to give directions to home given the directions to a destination where the starting point is home.

"""
import os

def main():
    cur_dir = os.getcwd()
    data_index = 3 # which test data fild is used

    datain = open(os.path.join(cur_dir,f"testing/j3.{data_index}.in"), "r").read().splitlines() # in data
    dataout = open(os.path.join(cur_dir,f"testing/j3.{data_index}.out"), "r").read().splitlines() # correct corresponding out data
    out = [] # program output

    data = datain
    data.reverse()
    data.append("HOME") # add home to the end as this is the destination

    # reverse list and reverse direcetions
    data = inverse_direction(data)

    # create readable text based on inverted list and directions
    out = create_home_directions(data)
    if testing(dataout, out):
        print('\n'.join(out))


def testing(dataout, out):
    # compare correct outputs and program output
    ok = None
    for a,i in zip(dataout, out):
        if a == i:
            print(":) good")
            ok = True
        else:
            print(":( Bad")
            print(f"correct output: {a}")
            print(f"your output: {i}")
            ok = False
    return ok

def create_home_directions(directions):
    dir = []
    for a,i in enumerate(directions):
        if directions[a+1] != "HOME" and (i =="R" or i =="L"): # if home is not next and it is a direction
            dir.append(f"Turn {'LEFT' if i == 'L' else 'RIGHT'} onto {directions[a+1]} street.") # turn onto street
        elif i == "R" or i == "L": # if home is next and direction
            dir.append(f"Turn {'LEFT' if i == 'L' else 'RIGHT'} into your HOME.") # turn into home
            return dir
    return False 

def inverse_direction(dir_list):
    reverse = {"R": "L", "L": "R"}
    new_list = []
    for i in dir_list:
        if i == "R" or i == "L":
            new_list.append(reverse[i]) # if direction inverse
        else:
            new_list.append(i) # if not add to list
    return new_list


if __name__ == "__main__":
    main()