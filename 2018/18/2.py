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

# print max_i, max_j
def print_grid():
	for j in xrange(max_j+1):
		s = ''
		for i in xrange(max_i+1):
			s += grid[i][j]
		print s

# print_grid()
num_mins = 1000000000
# num_mins = 1000
last_resource_val = None
past_grids = {}
resource_vals = []
for minute in xrange(1, num_mins+1):
	orig_grid = copy.deepcopy(grid)
	# print minute
	# print_grid()

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
	new_resource_val = num_wood * num_yard

	if new_resource_val in past_grids:
		found = False

		for poss_grid in past_grids[new_resource_val]:
			if poss_grid == grid:
				found = True

				print resource_vals
				index_of_cycle = resource_vals.index(new_resource_val)
				cycle_length = len(resource_vals)-index_of_cycle
				# ri = 0
				# for r in resource_vals:
				# 	print str(ri) + ": "+ str(r)
				# 	ri += 1
					# print resource_vals, len(resource_vals)

				answer = resource_vals[((num_mins-index_of_cycle-1)%cycle_length)+index_of_cycle]
				print answer, index_of_cycle, cycle_length
				sys.exit()

		if not found:
			past_grids[new_resource_val].append(copy.deepcopy(grid))
	else:
		past_grids[new_resource_val] = []
		past_grids[new_resource_val].append(copy.deepcopy(grid))

	resource_vals.append(new_resource_val)

print new_resource_val



# 45627, 34383, 79716

