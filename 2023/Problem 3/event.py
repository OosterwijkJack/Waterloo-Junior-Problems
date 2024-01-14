

def main():
    
    days = int(input())
    day_data = []

    for i in range(days):
        day_data.append(str(input()))
    

    day_data = [str(x).strip() for x in day_data] # days in list form
    count = (count_y_indices(day_data)) # count amount of Y's per list
    matches = (most_matches(count)) # put day matches in dict
    best_days = find_max(matches) # find best days from dict
    print(",".join([str(x) for x in best_days])) # output


def find_max(data: dict): # finds the days with the most Y's 
    cur_max = 0
    best_days = []
    for i in data:
        if data[i] > cur_max: # if people that can come on that day is more than current max
            cur_max = int(i) # set cur max to day

    best_days.append(cur_max+1) # append maximum day
    for i in data: # find any days with the same value as max and add to list
        if data[i] == cur_max:
            if int(i) + 1 not in best_days:
                best_days.append(int(i)+1)
    return sorted(best_days)
    

def most_matches(data:list): # return dictionary that holds days and matches per day
    nums = {}

    for i in data:
        for a in i:
            if str(a) in nums:
                nums[str(a)] += 1 # str cause easier to read
            else:
                nums[str(a)] = 1
    return nums

def count_y_indices(data: list):
    indicies = []
    for i in data: # loop list
        total = []
        for a in range(len(i)): # loop str
            if i[a] == "Y": # if Y
                total.append(a) # append the day index
        indicies.append(total) # add all to list
    return indicies




if __name__ == "__main__":
    main()