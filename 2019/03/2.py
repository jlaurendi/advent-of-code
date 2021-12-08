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
    steps = 0
    for l in wire:
        old_x = x
        old_y = y
        (x, y) = parse_step(l, x, y)
        x_sign = int(math.copysign(1, x - old_x))
        y_sign = int(math.copysign(1, y - old_y))

        for i in xrange(old_x, x + x_sign, x_sign):
            for j in xrange(old_y, y + y_sign, y_sign):
                if i == old_x and j == old_y:
                    continue

                steps += 1
                if j not in grid:
                    grid[j] = {}
                grid[j][i] = steps


    return grid

grid0 = convert_to_grid(wires[0])

intersections = []
x = 0
y = 0
steps = 0
for l in wires[1]:
    old_x = x
    old_y = y
    (x, y) = parse_step(l, x, y)
    x_sign = int(math.copysign(1, x - old_x))
    y_sign = int(math.copysign(1, y - old_y))

    for i in xrange(old_x, x + x_sign, x_sign):
        for j in xrange(old_y, y + y_sign, y_sign):
            if i == old_x and j == old_y:
                continue
            steps += 1
            if j in grid0 and i in grid0[j]:
                intersections.append((i, j, steps + grid0[j][i]))


min_steps = None
for isect in intersections:
    (x, y, steps) = isect
    if x == 0 and y == 0:
        continue
    if (min_steps == None or steps < min_steps): 
        min_steps = steps
        
print(min_steps)


# 101967
# 101961