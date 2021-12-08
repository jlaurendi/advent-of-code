import sys, copy

n = 3628

def power_level(x, y, n):
	return ((x+10)*(y*(x+10)+n) / 100) % 10 - 5

xlimit = 300
ylimit = 300

grid = {}

curr_max = 0
max_xy = None

for i in xrange(xlimit):
	for j in xrange(ylimit):
		if i not in grid:
			grid[i] = {}
		grid[i][j] = power_level(i, j, n)


for i in xrange(xlimit):
	for j in xrange(ylimit):
		if i not in grid:
			grid[i] = {}
		grid[i][j] = power_level(i, j, n)



# for size in xrange(1, 301):
# 	for i in xrange(xlimit-size+1):
# 		for j in xrange(ylimit-size+1):
# 			curr_total_power = 0
# 			for k in range(size):
# 				for l in range(size):
# 					curr_total_power += grid[i+k][j+l]
# 			if curr_total_power > curr_max:
# 				curr_max = curr_total_power
# 				max_xy = (i, j, size)

# print curr_max, max_xy

for i in xrange(300):
	for j in xrange(300):
		curr_sum = grid[i][j]
		size = 1
		if curr_sum > curr_max:
			curr_max = curr_sum
			max_xy = (i, j, size)

		while True:
			size += 1
			if i+size-1 >= 300 or j+size-1 >= 300:
				break

			for k in xrange(size):
				curr_sum += grid[i+size-1][j+k]
				curr_sum += grid[i+k][j+size-1]
			curr_sum -= grid[i+size-1][j+size-1]

			if curr_sum > curr_max:
				curr_max = curr_sum
				max_xy = (i, j, size)

print curr_max, max_xy