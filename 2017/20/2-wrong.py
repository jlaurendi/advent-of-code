import sys, math
with open('advent-input.txt') as f:
# with open('avent-test.txt') as f:
    a = f.readlines()


pos = []
vel = []
acc = []
order = []
parts = []
idx = 0
for ln in a:
	p,v,a = ln.split(', ')
	p = p.replace("<","").replace(">","").replace('p=','').split(',')
	v = v.replace("<","").replace(">","").replace('v=','').split(',')
	a = a.replace("<","").replace(">","").replace('a=','').split(',')

	p = [int(i) for i in p]
	v = [int(i) for i in v]
	a = [int(i) for i in a]

	pos.append(p)
	vel.append(v)
	acc.append(a)
	parts.append(idx)
	idx+=1

def check_equal(p0, v0, a0, p1, v1, a1, t):
	a = .5 * (a0+v0-a1-v1)
	b = .5 * (v0-v1+(a1-a0))
	c = p0-p1
	res = a*t**2+b*t+c
	return res == 0

def calc_collisions(p0, v0, a0, p1, v1, a1):

	if a0+v0 == a1+v1:
		if v0 == v1:
			if p0 == p1:
				return ['all']
			else:
				return []

		val0 = (p1-p0)*1.0/(v0-v1)
		val0 = math.floor(val0)
		ret = []

		try1 = val0
		while check_equal(p0, v0, a0, p1, v1, a1, try1):
			if try1 >= 0:
				ret.append(try1)
			try1 -= 1
			break

		try1 = val0+1
		while check_equal(p0, v0, a0, p1, v1, a1, try1):
			if try1 >= 0:
				ret.append(try1)
			try1 += 1
			break

		if p0 == p1:
			try1 = 0
			while check_equal(p0, v0, a0, p1, v1, a1, try1):
				if try1 >= 0:
					ret.append(try1)
				try1 += 1
				break
			
		return ret

	a = .5 * (a0+v0-a1-v1)
	b = .5 * (v0-v1+(a1-a0))
	c = p0-p1
	det = b**2 - 4*a*c
	if det < 0:
		return []
	val1 = -1.0 * b + det**.5
	val1 = val1 / (2*a)
	val2 = -1.0 * b - det**.5
	val2 = val2 / (2*a)

	ret = []
	val1 = math.floor(val1)
	val2 = math.floor(val2)

	# check val 1
	try1 = val1
	while check_equal(p0, v0, a0, p1, v1, a1, try1):
		if try1 >= 0:
			ret.append(try1)
		try1 -= 1
		break

	try1 = val1+1
	while check_equal(p0, v0, a0, p1, v1, a1, try1):
		if try1 >= 0:
			ret.append(try1)
		try1 += 1
		break


	try1 = val2
	while check_equal(p0, v0, a0, p1, v1, a1, try1):
		if try1 >= 0:
			ret.append(try1)
		try1 -= 1
		break

	try1 = val2+1
	while check_equal(p0, v0, a0, p1, v1, a1, try1):
		if try1 >= 0:
			ret.append(try1)
		try1 += 1
		break

	if p0 == p1:
		ret.append(0)

	return ret

def calc_full_collision(i, j):
	curr_cols = set()
	k=0
	cols0 = calc_collisions(pos[i][k], vel[i][k], acc[i][k], pos[j][k], vel[j][k], acc[j][k])
	k=1
	cols1 = calc_collisions(pos[i][k], vel[i][k], acc[i][k], pos[j][k], vel[j][k], acc[j][k])
	k=2
	cols2 = calc_collisions(pos[i][k], vel[i][k], acc[i][k], pos[j][k], vel[j][k], acc[j][k])

	if len(cols0) == 0 or len(cols1) == 0 or len(cols2) == 0:
		return None

	cols_set = set()
	if 'all' in cols0:
		if 'all' in cols1:
			if 'all' in cols2:
				return 0
			else:
				cols1 = cols2

		cols0 = cols1
	elif 'all' in cols1:
		if 'all' in cols2:
			cols1 = cols0
			cols2 = cols0
		else:
			cols1 = cols0
	elif 'all' in cols2:
		cols2 = cols1


	cols_set = set(cols0)
	cols_set = cols_set.intersection(cols1)
	cols_set = cols_set.intersection(cols2)
	cols_set = [c for c in cols_set if c.is_integer()]
	if len(cols_set) > 0:
		return min(cols_set)
	else:
		return None

	# for k in range(3):
	# 	cols = calc_collisions(pos[i][k], vel[i][k], acc[i][k], pos[j][k], vel[j][k], acc[j][k])
	# 	if len(cols) == 0:
	# 		return None
	# 	else:
	# 		if k == 0:
	# 			curr_cols = set(cols)
	# 		else:
	# 			if 'all' in cols:
	# 				print k
	# 				continue
	# 			else:
	# 				print curr_cols,cols,k
	# 				curr_cols = curr_cols.intersection(cols)
	# 				print curr_cols
	# if len(curr_cols) == 0:
	# 	return None
	# else:
	# 	print i,j,curr_cols
	# 	return min(curr_cols)

collisions = {}
col_times = set()
for i in parts:
	collisions[i] = {}
	for j in parts:
		if i == j:
			continue
		col = calc_full_collision(i, j)
		if col != None:
			if col == 'all':
				col = 0
			if col.is_integer():
				collisions[i][j] = int(col)
				col_times.add(int(col))

# print collisions


for i in col_times:
	del_this_round = []
	for j in collisions:
		if j not in parts:
			continue

		for k in collisions[j]:
			if (k in parts or k in del_this_round) and collisions[j][k] == i:
				if j in parts:
					del parts[parts.index(j)]
					del_this_round.append(j)



print len(parts)

