import sys, copy

grid = {}
max_i = 0
max_j = 0
with open('advent-input.txt') as f:
	a = f.readlines()

	j = 0
	for line in a:
		line = line.strip()
		i = 0
		for char in line:
			if i not in grid:
				grid[i] = {}
			grid[i][j] = char
			max_i = max(max_i, i)
			i += 1
		max_j = max(max_j, j)
		j += 1

print max_i, max_j
def print_grid():
	for j in xrange(max_j+1):
		s = ''
		for i in xrange(max_i+1):
			s += grid[i][j]
		print s

print_grid()
num_mins = 10

for minute in range(num_mins):
	orig_grid = copy.deepcopy(grid)
	print minute
	print_grid()

	for i in xrange(max_i+1):
		for j in xrange(max_j+1):
			adj_cells = [
				(i-1,j),
				(i-1,j-1),
				(i-1,j+1),
				(i,j-1),
				(i,j+1),
				(i+1,j-1),
				(i+1,j),
				(i+1,j+1)
			]

			adj_trees = 0
			adj_lumber = 0
			for (x,y) in adj_cells:
				if x > max_i or x < 0 or y > max_j or y < 0:
					continue


				if orig_grid[x][y] == '|':
					if i== 8 and j == 0:
						print x,y, orig_grid

					adj_trees += 1
				elif orig_grid[x][y] == '#':
					adj_lumber += 1

			curr_val = orig_grid[i][j]
			new_val = curr_val
			if curr_val == '.' and adj_trees >= 3:
				new_val = '|'
			elif curr_val == '|' and adj_lumber >= 3:
				new_val = '#'
			elif curr_val == '#' and (adj_lumber == 0 or adj_trees == 0):
				new_val = '.'


			grid[i][j] = new_val


num_wood = 0
num_yard = 0

for i in xrange(max_i+1):
	for j in xrange(max_j+1):
		val = grid[i][j]
		if val == '|':
			num_wood += 1
		elif val == '#':
			num_yard += 1
print num_wood * num_yard