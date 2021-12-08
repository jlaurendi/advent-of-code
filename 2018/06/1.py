import sys
with open('advent-input.txt') as f:
	a = f.readlines()
	a = [i.strip().split(', ') for i in a]
	a = [(int(x), int(y)) for (x,y) in a]

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

closest = {}
xrange1 = minx - abs(maxy-miny)
xrange2 = maxx + abs(maxy-miny)
yrange1 = miny - abs(maxx-minx)
yrange2 = maxy + abs(maxx-minx)
for i in xrange(xrange1, xrange2):
	for j in xrange(miny, maxy):

		dupe = False
		curr_min_node = None
		curr_min_value = None
		for k in xrange(len(a)):
			(i2, j2) = a[k]

			dist = abs(i2-i) + abs(j2-j)
			if dist == curr_min_value:
				dupe = True
			elif dist < curr_min_value or curr_min_value == None:
				curr_min_value = dist
				curr_min_node = k
				dupe = False

		if curr_min_value != None and not dupe:
			closest[(i, j)] = curr_min_node

def is_infinite(a, val):
	(i2, j2) = a[val]

	if i2 == minx or i2 == maxx or j2 == miny or j2 == maxy:
		return True

	left_bound = False
	right_bound = False
	top_bound = False
	bottom_bound = False

	for (i, j) in a:
		if i == i2 and j == j2:
			continue

		if i2 >= i and abs(j2-j) <= abs(i2-i):
			left_bound = True
		if i >= i2 and abs(j2-j) <= abs(i2-i):
			right_bound = True
		if j2 >= j and abs(i2-i) <= abs(j2-j):
			top_bound = True
		if j >= j2 and abs(i2-i) <= abs(j2-j):
			bottom_bound = True

	finite = left_bound and right_bound and top_bound and bottom_bound
	return not finite

areas_by_k = {}
for (i, j) in closest:

	val = closest[(i, j)]
	if is_infinite(a, val):
		continue

	if val not in areas_by_k:
		areas_by_k[val] = 0

	areas_by_k[val] += 1

print max(areas_by_k.values())
