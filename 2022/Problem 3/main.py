def main(data):
    tunes = (seperate_tunes(data))
    print(output_tunes(tunes))

def output_tunes(tunes):
    out = ""
    for i in tunes:
        operator = i.find("+") if "+" in i else i.find("-") # find operator
        notes = i[0:operator] # notes 
        out += f"{notes} {'tighten' if i[operator] == '+' else 'loosen'} {i[operator+1]}\n" 
    return out

def seperate_tunes(tunes: str): # seperates tunes into list of each tweak
    out = []
    while len(tunes) > 0: # while entire string hasnt been checked
        # find either add or subtract
        add = tunes.find("+")
        sub = tunes.find("-")
        
        # if both dont equal -1
        if add != -1 and sub != -1:
            small = min(add,sub) 
        else:
            if add == -1: # assign smallest as value that dosent equal -1
                small = sub
            elif sub == -1:
                small = add
        small += 2 # add 2 to index

        out.append(tunes[0:small]) # entire tune and tweak
        tunes = tunes.replace(tunes[0:small], "") # remove tune from string that has been added to list
    return out


main("AFB+8SC-4H-2GDPE+9")