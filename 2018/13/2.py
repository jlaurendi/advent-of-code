import sys, copy
with open('advent-input.txt') as f:
	a = f.readlines()
	a = [i.strip('\n') for i in a]

grid = {}
carts = []
cart_locs = {}

for j in xrange(len(a)):
	print a[j]
	for i in xrange(len(a[j])):
		val = a[j][i]

		if val == ' ':
			continue

		if val in ['v', '>', '<', '^']:
			carts.append([i,j,val,0])
			if i not in cart_locs:
				cart_locs[i] = {}
			cart_locs[i][j] = 1

		grid_val = val
		if val == 'v' or val == '^':
			grid_val = '|'
		elif val == '<' or val == '>':
			grid_val = '-'

		if i not in grid:
			grid[i] = {}
		grid[i][j] = grid_val


num_carts = len(carts)
while True:
	# print cart_locs
	carts = sorted(carts, key=lambda x: (x[1], x[0]))

	c_index = 0
	for c in carts:
		if c == None:
			c_index += 1
			continue

		curr_i = c[0]
		curr_j = c[1]
		curr_dir = c[2]
		t = c[3]
		grid_elt = grid[curr_i][curr_j]

		new_dir = curr_dir
		new_i = curr_i
		new_j = curr_j
		if grid_elt == '-':
			if curr_dir == '>':
				new_i = curr_i+1
			else:
				new_i = curr_i-1
		elif grid_elt == '|':
			if curr_dir == '^':
				new_j = curr_j-1
			else:
				new_j = curr_j+1
		elif grid_elt == "/":
			if curr_dir == '>':
				new_dir = '^'
				new_j = curr_j-1
			elif curr_dir == '<':
				new_dir = 'v'
				new_j = curr_j+1
			elif curr_dir == 'v':
				new_dir = '<'
				new_i = curr_i-1
			elif curr_dir == '^':
				new_dir = '>'
				new_i = curr_i+1
		elif grid_elt == "\\":
			if curr_dir == '>':
				new_dir = 'v'
				new_j = curr_j+1
			elif curr_dir == '<':
				new_dir = '^'
				new_j = curr_j-1
			elif curr_dir == 'v':
				new_dir = '>'
				new_i = curr_i+1
			elif curr_dir == '^':
				new_dir = '<'
				new_i = curr_i-1
		elif grid_elt == "+":
			if t == 0: # left
				if curr_dir == '>':
					new_dir = '^'
					new_j = curr_j-1
				elif curr_dir == '<':
					new_dir = 'v'
					new_j = curr_j+1
				elif curr_dir == 'v':
					new_dir = '>'
					new_i = curr_i+1
				elif curr_dir == '^':
					new_dir = '<'
					new_i = curr_i-1

			elif t == 1: # straight
				if curr_dir == '>':
					new_i = curr_i+1
				elif curr_dir == '<':
					new_i = curr_i-1
				elif curr_dir == 'v':
					new_j = curr_j+1
				elif curr_dir == '^':
					new_j = curr_j-1

			elif t == 2: # right
				if curr_dir == '>':
					new_dir = 'v'
					new_j = curr_j+1
				elif curr_dir == '<':
					new_dir = '^'
					new_j = curr_j-1
				elif curr_dir == 'v':
					new_dir = '<'
					new_i = curr_i-1
				elif curr_dir == '^':
					new_dir = '>'
					new_i = curr_i+1

			carts[c_index][3] = (t + 1) % 3

		# Check collision
		if new_i in cart_locs and new_j in cart_locs[new_i] and cart_locs[new_i][new_j] != None:
			carts[c_index] = None
			carts[cart_locs[new_i][new_j]] = None
			cart_locs[curr_i][curr_j] = None
			cart_locs[new_i][new_j] = None
			num_carts -= 2

		else:
			cart_locs[curr_i][curr_j] = None
			if new_i not in cart_locs:
				cart_locs[new_i] = {}
			cart_locs[new_i][new_j] = c_index

			carts[c_index][0] = new_i
			carts[c_index][1] = new_j
			carts[c_index][2] = new_dir

		c_index += 1

	new_carts = []
	for c in carts:
		if c != None:
			new_carts.append(c)
	carts = new_carts

	if num_carts == 1:
		# print carts
		for c in carts:
			if c != None:
				print c
		sys.exit()