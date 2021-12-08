import sys
with open('advent-input.txt') as f:
	a = f.readlines()
	a = [i.split('@')[1].strip() for i in a]

grid = {}
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
				grid[x_coord][y_coord] = 1
			else:
				grid[x_coord][y_coord] += 1

count = 0
for row in grid.keys():
	for elt in grid[row].keys():
		if grid[row][elt] > 1:
			count += 1

print(count)




sys.exit()