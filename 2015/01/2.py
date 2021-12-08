import sys

# with open('input-test.txt') as f:
with open('input.txt') as f:
    a = f.readlines()
    # a = ')())())'
    # a = '))((((('

    floor = 0
    position = 1
    for i in a:
        for char in i:
            if char == '(':
                floor += 1
                position += 1
            elif char == ')':
                floor -= 1
                position += 1

            if floor < 0:
                print(position-1)
                sys.exit()

print(floor)