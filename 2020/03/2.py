import sys, os, copy
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

grid = {}
with open(input_path) as f:
    lns = f.readlines()

    for i in range(len(lns)):
        grid[i] = {}
        ln = lns[i].strip()

        for j in range(len(ln)):
            grid[i][j] = ln[j] == '#'

def calc_num_tree(slope):
    (slope_x, slope_y) = slope
    curr_x = 0
    curr_y = 0

    max_x = len(grid[0])
    max_y = len(grid)
    num_trees = 0
    while True:
        curr_y += slope_y
        curr_x += slope_x

        if curr_y >= max_y:
            break

        if grid[curr_y][curr_x % max_x]:
            num_trees += 1

    return num_trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1
for slope in slopes:
    result *= calc_num_tree(slope)
print(result)