import sys, copy



def print_grid():
	for j in range(j_range):
		s = ''
		for i in range(i_range):
			s += str(grid[i][j])

		print s

grid = {}
goblins = {}
elves = {}
g_index = 0
e_index = 0
i_range = None
j_range = None
with open('advent-input.txt') as f:
	a = f.readlines()

	j = 0
	for line in a:
		line = line.strip()
		i = 0
		for c in line:
			if c == 'G':
				if i not in goblins:
					goblins[i] = {}
				goblins[i][j] = ['G', g_index, i, j, 200]
				g_index += 1
			elif c == 'E':
				if i not in elves:
					elves[i] = {}
				elves[i][j] = ['E', e_index, i, j, 200]
				e_index += 1

			if i not in grid:
				grid[i] = {}
			grid[i][j] = c
			i += 1
		j += 1

	i_range = i
	j_range = j


def check_game_over():
	num_goblins = 0
	for i in goblins:
		num_goblins += len(goblins[i])

	num_elves = 0
	for i in elves:
		num_elves += len(elves[i])

	if num_goblins > 0 and num_elves > 0:
		return False

	hit_points_remaining = 0
	goblin_pts = 0
	elf_pts = 0
	for i in goblins:
		for g in goblins[i].values():
			goblin_pts += g[4]
			hit_points_remaining += g[4]
	for i in elves:
		for e in elves[i].values():
			hit_points_remaining += e[4]
			elf_pts += e[4]

	# print_grid()
	# print num_full_rounds, hit_points_remaining
	print num_full_rounds * hit_points_remaining
	return 'E' if elf_pts > 0 else 'G'

def determine_square_to_attack(curr_i, curr_j, curr_type):
	enemy_type = 'E' if curr_type == 'G' else 'G'

	attack_locations = [(curr_i, curr_j-1), (curr_i-1, curr_j), (curr_i+1, curr_j),  (curr_i, curr_j+1)]
	attack_options = []

	for (i, j) in attack_locations:
		if i < 0 or j < 0 or i >= len(grid[0]) or j >= len(grid):
			continue

		if grid[i][j] == enemy_type:
			if enemy_type == 'G':
				attack_options.append(goblins[i][j])
			else:
				attack_options.append(elves[i][j])


	if len(attack_options) == 0:
		return None

	# print attack_options
	attack_options = sorted(attack_options, key=lambda x: (x[4], x[3], x[2]))
	return attack_options[0]

def take_move(curr_i, curr_j, curr_type):
	curr_paths = [[(curr_i,curr_j)]]
	enemy_type = 'E' if curr_type == 'G' else 'G'
	enemies = elves if enemy_type == 'E' else goblins

	possible_nodes = []
	for enum in enemies:
		for eenum in enemies[enum]:
			enemy = enemies[enum][eenum]
			i = enemy[2]
			j = enemy[3]
			next_step_options = [(i, j-1), (i-1, j), (i+1, j),  (i, j+1)]
			for (next_i, next_j) in next_step_options:
				if grid[next_i][next_j] == '.':
					possible_nodes.append((next_i,next_j))

	# print possible_nodes
	nodes_reached = {}
	nodes_reached[(curr_i, curr_j)] = 1

	good_paths = []
	while len(curr_paths) > 0:
		# print curr_i,curr_j
		# if curr_i == 2 and curr_j == 1:
		# 	print curr_paths
		p = curr_paths.pop(0)
		if len(good_paths) > 0 and len(p) == len(good_paths[0]):
			break
		i = p[-1][0]
		j = p[-1][1]
		next_step_options = [(i, j-1), (i-1, j), (i+1, j),  (i, j+1)]
		for (next_i, next_j) in next_step_options:
			if (next_i, next_j) in nodes_reached:
				continue
			curr_grid_value = grid[next_i][next_j]
			if (next_i,next_j) in possible_nodes:
				p.append((next_i,next_j))
				good_paths.append(p)
			elif curr_grid_value == '.':
				pcopy = p[:]
				pcopy.append((next_i, next_j))
				curr_paths.append(pcopy)
				nodes_reached[(next_i, next_j)] = 1

	if len(good_paths) > 0:

		good_paths = sorted(good_paths, key=lambda x: (x[-1][1], x[-1][0]))

		p = good_paths[0]
		new_i,new_j = p[1]
		if curr_type == 'G':
			if new_i not in goblins:
				goblins[new_i] = {}
			goblins[new_i][new_j] = goblins[curr_i][curr_j]
			goblins[new_i][new_j][2] = new_i
			goblins[new_i][new_j][3] = new_j
			goblins[curr_i].pop(curr_j, None)
		else:
			if new_i not in elves:
				elves[new_i] = {}
			elves[new_i][new_j] = elves[curr_i][curr_j]
			elves[new_i][new_j][2] = new_i
			elves[new_i][new_j][3] = new_j
			elves[curr_i].pop(curr_j, None)

		grid[new_i][new_j] = curr_type
		grid[curr_i][curr_j] = '.'
		return (new_i, new_j)



orig_grid = copy.deepcopy(grid)
orig_goblins = copy.deepcopy(goblins)
orig_elves = copy.deepcopy(elves)
elf_power = 4
while True:
	ticks = 0
	grid = copy.deepcopy(orig_grid)
	goblins = copy.deepcopy(orig_goblins)
	elves = copy.deepcopy(orig_elves)
	game_over = False
	num_full_rounds = 0

	num_starting_elves = 0
	for ei in elves:
		num_starting_elves += len(elves[ei])

	while True:
		ticks += 1
		# if ticks == 10:
		# 	sys.exit()
		# print ticks
		all_units = []
		for i in goblins:
			all_units += goblins[i].values()
		for i in elves:
			all_units += elves[i].values()
		all_units = sorted(all_units, key=lambda x: (x[3], x[2]))

		for unit in all_units:
			curr_type = unit[0]
			curr_i = unit[2]
			curr_j = unit[3]

			if curr_type == 'G' and (curr_i not in goblins or curr_j not in goblins[curr_i]):
				continue
			if curr_type == 'E' and (curr_i not in elves or curr_j not in elves[curr_i]):
				continue

			winner = check_game_over()
			# print winner, elf_power
			if winner != False:
				game_over = True
				break

			unit_to_attack = determine_square_to_attack(curr_i, curr_j, curr_type)

			if unit_to_attack == None:
				move = take_move(curr_i, curr_j, curr_type)
				new_i = curr_i
				new_j = curr_j
				if type(move) is tuple:
					new_i, new_j = move
					unit_to_attack = determine_square_to_attack(new_i, new_j, curr_type)

			if unit_to_attack != None:
				i = unit_to_attack[2]
				j = unit_to_attack[3]
				if i in goblins and j in goblins[i]:
						goblins[i][j][4] -= elf_power
						if goblins[i][j][4] <= 0:
							goblins[i].pop(j, None)
							grid[i][j] = '.'

				else:
					elves[i][j][4] -= 3
					if elves[i][j][4] <= 0:
						elves[i].pop(j, None)
						grid[i][j] = '.'

		if game_over:
			break

		num_full_rounds += 1
		# print_grid()
		# print elves, goblins, num_full_rounds

	num_elves_left = 0
	for ei in elves:
		num_elves_left += len(elves[ei].values())

	print elves, num_elves_left, num_starting_elves
	print orig_elves
	if winner == 'E' and num_elves_left == num_starting_elves:
		print elf_power
		sys.exit()
	elf_power += 1


# guesses: 179220, 179220, 178003
