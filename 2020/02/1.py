import sys, os, copy
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

passwords = []
with open(input_path) as f:
    lns = f.readlines()
    for ln in lns:
        # split first on the : 
        split =  ln.strip().split(':')
        left = split[0]
        password = split[1].strip()

        # split again on the space
        split = left.split(' ')
        left = split[0].strip()
        char = split[1]

        (min_occur, max_occur) = [int(elt) for elt in left.split('-')]
        
        row = [min_occur, max_occur, char, password]        
        passwords.append(row)


num_valid = 0
for (min_occur, max_occur, char, password) in passwords:
    num_occur = 0
    for ch in password:
        if ch == char:
            num_occur += 1

    if num_occur >= min_occur and num_occur <= max_occur:
        num_valid += 1

print(num_valid)
