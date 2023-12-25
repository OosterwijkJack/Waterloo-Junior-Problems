import os
# The Cell Sell
"""
The function of this program is to caclulate the best cell phone usage plan for Moe Bull

"""

def main():
    here = os.getcwd()
    data_index = 3 # which test data fild is used

    datain = open(os.path.join(here,f"testing/j1.{data_index}.in"), "r").read().splitlines() # in data
    dataout = open(os.path.join(here,f"testing/j1.{data_index}.out"), "r").read().splitlines() # correct corresponding out data
    out = [] # program output

    day = int(datain[0])
    even = int(datain[1])
    week = int(datain[2])
    # calculate plan A
    A_cost = A_price(day,even,week)
    # calculate plan B
    B_cost = B_price(day,even,week)

    # output placed in out list used later to check if correct
    out.append(f"Plan A costs {A_cost}") 
    out.append(f"Plan B costs {B_cost}")

    if  A_cost == B_cost:
        out.append("Plan A and B are the same price.")
    else:
        out.append("Plan A is cheapest." if A_cost < B_cost else "Plan B is cheapest.")

    if testing(dataout, out):
        display(out)

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

def display(out):
    print('\n'.join(out))

def A_price(day, evening, weekend):
    # 100 free minutes then 25 cents a minute
    if day > 100:
        day = (day-100) * 0.25
    else:
        day = 0

    evening = evening * 0.15 # 15 cents a minute
    weekend = weekend * 0.20 # 20 cents a minute

    a = (day, evening,weekend)
    return round(sum(a),2) # sum the values and round to second decimal place
    
def B_price(day, evening, weekend):
    if day > 250:
        day = (day-250) * 0.45
    else:
        day = 0

    evening = evening * 0.35
    weekend = weekend * 0.25

    a = (day,evening,weekend)
    return round(sum(a),2) # sum the values and round to second decimal place

if __name__ == "__main__":
    main() 