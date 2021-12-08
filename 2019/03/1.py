import sys, os, copy, math
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'advent-input.txt')


with open(input_path) as f:
    lines = f.readlines()
    wires = []
    for i in xrange(len(lines)):
        wires.append([])
        for d in lines[i].split(','):
            wires[i].append((d[0], int(d[1:])))

def parse_step(l, x, y):
    dir = l[0]
    num_steps = l[1]
    if dir == 'D':
        y -= num_steps
    elif dir == 'U':
        y += num_steps
    elif dir == 'L':
        x -= num_steps
    elif dir == 'R':
        x += num_steps
    return (x, y)

def convert_to_grid(wire):
    x = 0
    y = 0
    grid = {}
    for l in wire:
        old_x = x
        old_y = y
        (x, y) = parse_step(l, x, y)
        x_sign = int(math.copysign(1, x - old_x))
        y_sign = int(math.copysign(1, y - old_y))

        for i in xrange(old_x, x + 1, x_sign):
            for j in xrange(old_y, y + 1, y_sign):
                if j not in grid:
                    grid[j] = {}
                grid[j][i] = True

    return grid

grid0 = convert_to_grid(wires[0])

intersections = []
x = 0
y = 0
for l in wires[1]:
    old_x = x
    old_y = y
    (x, y) = parse_step(l, x, y)
    x_sign = int(math.copysign(1, x - old_x))
    y_sign = int(math.copysign(1, y - old_y))

    for i in xrange(old_x, x + 1, x_sign):
        for j in xrange(old_y, y + 1, y_sign):
            if j in grid0 and i in grid0[j]:
                intersections.append((i, j))
print intersections
min_d = None
for isect in intersections:
    (x, y) = isect
    if x == 0 and y == 0:
        continue
    curr_d = abs(x) + abs(y)
    if (min_d == None or curr_d < min_d): 
        min_d = curr_d
        
print(min_d)
