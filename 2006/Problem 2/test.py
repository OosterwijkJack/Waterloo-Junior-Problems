import dice
from pathlib import Path
import os


def main():  
    year = 2006
    problem = 2
    files = len(os.listdir(Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data"))) // 2
    correct = True
    for i in range(files):
        index = i+1

        datain = open(Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data/j{problem}.{index}.in")).read().splitlines()
        dataout = open(Path.joinpath(Path.cwd(), f"{year}/Problem {problem}/test_data/j{problem}.{index}.out")).read().splitlines()

        datain = [int(x) for x in datain]

        out = dice.begin(*datain)
        out = [out]
        if testing(dataout, out):
            print("\n".join(out))
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