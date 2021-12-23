import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__, 'input.txt')


def solve(input_path):
	with open(input_path) as f:
		lines = [ln.strip().split(' -> ') for ln in f.readlines()]
		lines = [[tuple(map(int, elt.split(','))) for elt in ln] for ln in lines ]
		lines = filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines)

	grid = {}
	for ln in lines:
		grid = process_line(ln, grid)

	count = 0
	# print_grid(grid)
	for i in grid:
		row = grid[i]

		for j in row:
			elt = row[j]
			if elt > 1:
				count += 1
	return count

def process_line(line, grid):
	(x1, y1) = line[0]
	(x2, y2) = line[1]

	if x1 != x2:
		direction = 1 if x1 < x2 else -1
		start = x1
		end = x2 + 1 if direction > 0 else x2 - 1
		for x in range(start, end, direction):
			if x not in grid:
				grid[x] = {}

			if y1 not in grid[x]:
				grid[x][y1] = 0

			grid[x][y1] += 1 

	if y1 != y2:
		direction = 1 if y1 < y2 else -1
		start = y1
		end = y2 + 1 if direction > 0 else y2 - 1
		for y in range(start, end, direction):
			if x1 not in grid:
				grid[x1] = {}

			if y not in grid[x1]:
				grid[x1][y] = 0

			grid[x1][y] += 1 

	return grid

def print_grid(grid):
	min_x, min_y = 0,0

	max_x = max(grid)
	max_y = max([max(grid[v]) for v in grid])

	for j in range(min_y, max_y + 1):
		line_out = ''
		for i in range(min_x, max_x + 1):
			if i in grid and j in grid[i]:
				line_out += str(grid[i][j])
			else:
				line_out += '.'

print(solve(input_path))
