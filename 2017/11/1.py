import sys, math
with open('advent-input.txt') as f:
    a = f.readlines()[0].split(',')

pos_n = 0
pos_e = 0
max_dist = 0
for s in a:
	if s == "s":
		pos_n -= 1
	elif s == "n":
		pos_n += 1
	elif s == "se":
		pos_e += 1
		pos_n -= .5
	elif s == "sw":
		pos_e -= 1
		pos_n -= .5
	elif s == "ne":
		pos_e += 1
		pos_n += .5		
	elif s == "nw":
		pos_e -= 1
		pos_n += .5

	e = math.ceil(math.fabs(pos_e))
	n = math.fabs(pos_n) - e/2
	d = e + math.ceil(n)

	if d > max_dist:
		max_dist = d 

print max_dist