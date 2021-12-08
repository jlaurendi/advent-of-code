import sys
with open('advent-input.txt') as f:
	a = f.readlines()
	a = [i.split('@')[1].strip() for i in a]


grid = {}
claim_num = 1
claims_left = range(1,1350)
for elt in a:
	parts = elt.split(': ')
	x,y = [int(e) for e in parts[0].split(',')]
	w,l = [int(e) for e in parts[1].split('x')]

	for i in xrange(w):
		for j in xrange(l):
			x_coord = x+i
			y_coord = y+j

			if x_coord not in grid:
				grid[x_coord] = {}

			if y_coord not in grid[x_coord]:
				grid[x_coord][y_coord] = {}

			grid[x_coord][y_coord][claim_num] = 1
	claim_num += 1

for i in grid.keys():
	for j in grid[i].keys():

		if len(grid[i][j].keys()) > 1:
			for c in grid[i][j].keys():
				if c in claims_left:
					claims_left.remove(c)

print claims_left

sys.exit()