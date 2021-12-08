
import sys, copy, math, time, os

positions = {}
velocities = {}

with open('advent-input.txt') as f:
	a = f.readlines()

	i = 0
	for line in a:
		b = line.split('position=')[1].strip()
		b = b.split(' velocity=')
		pos = [int(p.strip()) for p in b[0][1:-1].strip().split(',')]
		vel = [int(p.strip()) for p in b[1][1:-1].strip().split(',')]

		positions[i] = pos
		velocities[i] = vel

		i += 1



x_width = 100
y_width = 25
view_scale = 1.10

last_point_locs = {}
itr = 0
for i in xrange(10**6):
	point_locs = {}
	x_scale = None
	y_scale = None
	xmax = None
	ymax = None
	xmin = None
	ymin = None
	for p in positions:
		positions[p][0] += velocities[p][0]
		positions[p][1] += velocities[p][1]
		x = int(positions[p][0])
		y = int(positions[p][1])

		if x > xmax or xmax == None:
			xmax = x
		if x < xmin or xmin == None:
			xmin = x
		if y > ymax or ymax == None:
			ymax = y
		if y < ymin or ymin == None:
			ymin = y

	xmid = (xmax+xmin)/2
	ymid = (ymax+ymin)/2
	x_scale = (xmax - xmin)
	y_scale = (ymax - ymin)

	for p in positions:
		x = round(1.0 * (positions[p][0] - xmin) / x_scale * x_width)
		y = round(1.0 * (positions[p][1] - ymin) / y_scale * y_width)
		x = int(x)
		y = int(y)

		point_locs[(x,y)] = 1

	xaxismax = int(x_width * view_scale)
	yaxismax = int(y_width * view_scale)
	xaxismin = 0 - (xaxismax-x_width)
	yaxismin = 0 - (yaxismax-y_width)

	# print point_locs, positions
	# print ymin, ymax
	print_out = False
	for p in point_locs:
		if p not in last_point_locs:
			print_out = True
			break
	if print_out:
		itr += 1
		os.system('clear')
		for j in xrange(yaxismin, yaxismax):
			s = ''
			for ii in xrange(xaxismin, xaxismax):
				if (ii,j) in point_locs:
					s += '#'
				else:
					s += '.'
			print s
		print("Iter: ", itr)
		print i+1
		if itr == 267:
			sys.exit()

	last_point_locs = point_locs
