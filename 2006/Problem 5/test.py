import Othello
from pathlib import Path
import os


def main():  
    year = 2006
    problem = 5
    files = len(os.listdir(Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data"))) // 2
    correct = True
    for i in range(files):
        index = i+1
        
        if files > 1:
            datain_dir = Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data/j{problem}.{index}.in")
            dataout_dir = Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data/j{problem}.{index}.out")
        else:
            datain_dir = Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data/j{problem}.in")
            dataout_dir = Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data/j{problem}.out")


        datain = open(datain_dir).read()
        dataout = open(dataout_dir).read().split()

        dataout = [int(x) for x in dataout]

        out = Othello.begin(datain)
        input()

        if testing(dataout, out):
            out
        else: correct = False

    print("\nPROGRAM PASSED ALL TESTS! :)" if correct else "\nPROGRAM FAILED :(")


def testing(dataout, out):
    # compare correct outputs and program output
    good = None
    for a,i in zip(dataout, out):
        if a == i:
            print(":) good")
            good = True
        else:
            print(":( Bad")
            print(f"correct output: {a}")
            print(f"your output: {i}")
            good = False
    return good

if __name__ == "__main__":
    main()