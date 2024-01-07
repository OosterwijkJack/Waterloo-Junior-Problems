from dataclasses import dataclass
"""
Name: Canadian Calorie Counting

This progam outputs the total calories based on an order made at "Chip's Fast Food emprium"

"""
@dataclass
class FoodItems:
    choices = [
    {1: 461, 2: 431, 3: 420},
    {1: 100, 2: 57, 3: 70},
    {1: 130, 2: 160, 3: 118},
     {1: 167, 2: 266, 3: 75} 
    ]

def main():
    print("Welcome to Chip’s Fast Food Emporium")
    choice1 = input("Please enter a burger choice: ")
    choice2 = input("Please enter a side order choice: ")
    choice3 = input("Please enter a drink choice: ")
    choice4 = input("Please enter a dessert choice: ")

    print(begin(choice1,choice2,choice3,choice4)[0])

def begin(*data):
    cals = get_cal(*data)
    return [f"Your total calorie count is {cals[0]}."]
    

def get_cal(*data):
    total_cal = 0
    for a,i in enumerate(data):
        if int(i) == 4: continue

        total_cal += FoodItems.choices[a][int(i)]
    return [total_cal]   
if __name__ == "__main__":
    main()