import sys, copy

n = 3628

def power_level(x, y, n):
	return ((x+10)*(y*(x+10)+n) / 100) % 10 - 5

xlimit = 300
ylimit = 300

curr_max = 0
max_xy = None
for i in xrange(xlimit-2):
	for j in xrange(ylimit-2):
		curr_total_power = 0
		for k in range(3):
			for l in range(3):
				curr_total_power += power_level(i+k, j+l, n)
		if curr_total_power > curr_max:
			curr_max = curr_total_power
			max_xy = (i, j)

print curr_max, max_xy