import sys


def knot_hash(a):
	a = [ord(i) for i in a]
	a = a + [17, 31, 73, 47, 23]

	n = 256
	lst = range(n)
	pos = 0
	skip = 0
	for rnd in range(64):
		for l in a:

			for i in range(l/2):
				idx1 = (pos + i) % n
				idx2 = (pos + l - i - 1) % n
				tmp = lst[idx1]
				lst[idx1] = lst[idx2]
				lst[idx2] = tmp

			pos = (pos + l + skip) % n

			skip += 1

	dense = []
	for i in range(n/16):
		res = 0
		for j in range(16):
			res ^= lst[16*i+j]
		dense.append(res)

	knot = ""
	for c in dense:
		cc = hex(c)[2:]
		while len(cc) != 2:
			cc = "0" + cc
		knot += cc

	return knot

ipt = "stpzcrnm"
# ipt = "flqrgnkx"
num_open = 0
grid = []
num_groups = 0
equals = {}
for i in range(128):
	s = ipt + "-"+str(i)
	hsh = knot_hash(s)
	grid.append([])

	j = 0
	for char in hsh:
		char = int(char, 16)
		for k in range(4):

			if (char / 2**(3-k)) % 2 != 0:
				num_open += 1

				if i > 0 and grid[i-1][j] != 0: # top
					if j > 0 and grid[i][j-1] != 0 and grid[i][j-1] != grid[i-1][j]:
						lower = min(grid[i][j-1], grid[i-1][j])
						higher = max(grid[i][j-1], grid[i-1][j])
						for ii in range(len(grid)):
							for jj in range(len(grid[0])):
								if jj < len(grid[ii]) and grid[ii][jj] == higher:
									grid[ii][jj] = lower
						group = lower 
					else:
						group = grid[i-1][j]
				elif j > 0 and grid[i][j-1] != 0: # left
					group = grid[i][j-1]
				else:
					num_groups += 1
					group = num_groups

				grid[i].append(group)

			else:
				grid[i].append(0)

			char = char % 2**(3-k)
			j += 1

print num_open
unique = set()
for row in grid:
	for val in row:
		if val != 0:
			unique.add(val)
print len(unique)
sys.exit()

#print equals
print num_groups
print equals
print num_groups - len(equals)
sys.exit()