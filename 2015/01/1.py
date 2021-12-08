import sys

with open('input.txt') as f:
    a = f.readlines()
    # a = ')())())'
    # a = '))((((('

    floor = 0
    for i in a:
        for char in i:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1

print(floor)