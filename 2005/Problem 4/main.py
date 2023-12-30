"""
Name: Cross Spiral

The purpose of the program is to calculate the tile Bridget will be standing on given she walks a certain amount of steps
in a spiral within a cross within a room which dimensions are specified 

"""
import os

def main():
    cur_dir = os.getcwd()
    data_index = 3 # which test data fild is used

    datain = open(os.path.join(cur_dir,f"testing/j3.{data_index}.in"), "r").read().splitlines() # in data
    dataout = open(os.path.join(cur_dir,f"testing/j3.{data_index}.out"), "r").read().splitlines() # correct corresponding out data
    out = [] # program output


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


if __name__ == "__main__":
    main()