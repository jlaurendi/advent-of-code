from copy import deepcopy
data = open('input.txt').readlines()

def calc_dist(path, grid):
    total = 0
    for i in range(len(path)):
        total += grid[path[i]][path[(i+1)%len(path)]]
        total += grid[path[i]][path[(i-1)%len(path)]]
    return total

grid = {}
for line in data:
    line = line.split(' ')
    name1 = line[0]
    op = line[2]
    name2 = line[-1].strip().replace(".", "")

    pts = int(line[3])
    if op == 'lose':
        pts = -1 * pts

    if name1 not in grid:
        grid[name1] = {}

    grid[name1][name2] = pts

names = list(grid.keys())
num_names = len(names)
name1 = names.pop(0)
q = []
q.append([name1])
max_dist = 0
while len(q) > 0:
    curr_path = q.pop(0)

    for n in grid[curr_path[-1]]:
        if n in curr_path:
            continue

        curr_path_copy = deepcopy(curr_path)
        curr_path_copy.append(n)

        if len(curr_path_copy) == num_names:
            dist = calc_dist(curr_path_copy, grid)
            if dist > max_dist:
                max_dist = dist
        else:
            q.append(curr_path_copy)

print(max_dist)
print(grid)
# Guesses
# 452 too low