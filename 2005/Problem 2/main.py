import os
"""
RSA Numbers

The purpose of this program is to identify how many RSA numbers are in a range

"""

def main():
    here = os.getcwd()
    data_index = 3 # which test data fild is used

    datain = open(os.path.join(here,f"testing/j2.{data_index}.in"), "r").read().splitlines() # in data
    dataout = open(os.path.join(here,f"testing/j2.{data_index}.out"), "r").read().splitlines() # correct corresponding out data
    out = [] # program output

    lower_range = int(datain[0])
    upper_range = int(datain[1])

    valid = get_valid(lower_range, upper_range)
    out.append(f"The number of RSA numbers between {lower_range} and {upper_range} is {valid}.")

    if testing(dataout, out):
        print(out[0])

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

def get_valid(lower, upper):
    total_valid = 0
    for i in range(lower, upper+1): # add 1 range is not inclusive 
        if valid_RSA(i): # if number is a valid RSA add to total
            total_valid += 1
    return total_valid

def valid_RSA(number) ->bool:
    divs = 0
    for i in range(1,number+1):
        if number % i == 0: # check how many dividers the number has
            divs += 1

    if divs == 4: return True # if 4 that means it is a valid RSA
    else: return False
if __name__ == "__main__":
    main()