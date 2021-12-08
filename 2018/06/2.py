import sys
with open('advent-input.txt') as f:
	a = f.readlines()
	a = [i.strip().split(', ') for i in a]
	a = [(int(x), int(y)) for (x,y) in a]

size_threshold = 10000

minx = None
miny = None
maxx = None
maxy = None

for (i, j) in a:
	if minx == None:
		minx = i
		maxx = i
		miny = j
		maxy = j

	if i < minx:
		minx = i
	if i > maxx:
		maxx = i
	if j < miny:
		miny = j
	if j > maxy:
		maxy = j

region = {}
xrange1 = maxx - size_threshold
xrange2 = minx + size_threshold
yrange1 = maxy - size_threshold
yrange2 = miny + size_threshold
if xrange2 <= xrange1 or yrange2 <= yrange1:
	print 0
	sys.exit()
size = 0
xrange1 = minx
xrange2 = maxx
yrange1 = miny
yrange2 = maxy
for i in xrange(xrange1, xrange2):
	for j in xrange(yrange1, yrange2):

		total_distance = 0
		small_enough = True
		for k in xrange(len(a)):
			(i2, j2) = a[k]

			dist = abs(i2-i)+abs(j2-j)
			total_distance += dist
			if total_distance >= size_threshold:
				small_enough = False
				break

		if small_enough:
			region[(i,j)] = 1
			size += 1

print size
sys.exit()