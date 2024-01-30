"""

Name: Good Groups

1st line: the next X inputs will be two names and these two names MUST be in the same group. 
2nd line: the next Y inputs wild be two names and thest two names MUST NOT be in the same group.

3rd line: the next G lines will be 3 different names. this is a group

"""

def main():
    same = []
    for i in range(int(input())):
        same.append(input().split())
    sep = []
    for i in range(int(input())):
        sep.append(input().split())
    
    groups = []
    for i in range(int(input())):
        groups.append(input().split())

    violations = 0
    violations += same_group_violation(same,groups)
    violations += sep_groups_violation(sep, groups)

    print(violations)

def same_group_violation(same, groups: list):
    violations = 0
    good_groups = []

    for i in groups:
        for a in same:
            if a[0] in i and a[1] in i: # in same group
                good_groups.append([a[0], a[1]]) # add to good group


    if (good_groups) == (same): # if no violations
        return 0      
           
    violations = len(same) - (len(remove_duplicates(good_groups))) # amount of rules - amount of violations

    
    return violations
    
        
def sep_groups_violation(sep,groups):
    violations = 0
    good_groups = []

    for i in groups:
        for a in sep:
            if (a[0] in i and a[1] not in i) or (a[1] in i and a[0] not in i): # not in the same group
                good_groups.append([a[0], a[1]])
    
    if good_groups == sep:
        return 0
    violations += len(sep) - (len(remove_duplicates(good_groups)))
    
    return violations

def remove_duplicates(data):
    seen = []

    for i in data:
        if i not in seen:
            seen.append(i)
    return seen
main()