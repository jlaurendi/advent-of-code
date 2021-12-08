import sys,math,copy
with open('advent-input.txt') as f:
#with open('advent-test.txt') as f:
    a = f.readlines()

def flipx(a):
	a = string_to_array(a)
	l = len(a)
	flip = copy.deepcopy(a)
	for i in range(l):
		for j in range(l):
			flip[i][j] = a[l-i-1][j]
	return array_to_string(flip)

def flipy(a):
	a = string_to_array(a)
	l = len(a)
	flip = copy.deepcopy(a)
	for i in range(l):
		for j in range(l):
			flip[i][j] = a[i][l-j-1]
	return array_to_string(flip)

def rotate(a):
	a = string_to_array(a)
	l = len(a)
	flip = copy.deepcopy(a)
	for i in range(l):
		for j in range(l):
			flip[i][j] = a[j][l-1-i]

	return array_to_string(flip)

def array_to_string(a):
	s = ''
	for row in a:
		for val in row:
			s += val
	return s

def string_to_array(s):
	l = int(len(s)**.5)
	a = []
	for i in range(l):
		row = []
		for j in range(l):
			row.append(s[l*i+j])
		a.append(row)

	return a

rules = {}
for ln in a:

	inp,out = ln.split(" => ")

	inp = inp.replace('/','')
	out = out.replace('/','').replace('\n','')
	rules[inp] = out

	rules[rotate(inp)] = out
	rules[rotate(rotate(inp))] = out
	rules[rotate(rotate(rotate(inp)))] = out


	inp = flipx(inp)
	rules[flipx(inp)] = out
	rules[rotate(inp)] = out
	rules[rotate(rotate(inp))] = out
	rules[rotate(rotate(rotate(inp)))] = out

	inp = flipy(inp)
	rules[rotate(inp)] = out
	rules[rotate(rotate(inp))] = out
	rules[rotate(rotate(rotate(inp)))] = out

	inp = flipx(inp)
	rules[rotate(inp)] = out
	rules[rotate(rotate(inp))] = out
	rules[rotate(rotate(rotate(inp)))] = out

grid = {0:{0:'.',1:'#',2:'.'},1:{0:'.',1:'.',2:'#'},2:{0:'#',1:'#',2:'#'}}
for i in xrange(18):
	new_grid = {}
	if len(grid[0]) % 2 == 0:
		for i in range(len(grid[0])/2):
			for j in range(len(grid[0])/2):
				sub_grid = []
				for ii in range(2):
					sgr = []
					for jj in range(2):
						sgr.append(grid[2*i+ii][2*j+jj])
					sub_grid.append(sgr)
				# sub_grid = grid[3*i:3*i+3][3*j:3*j+3]
				sub_grid = array_to_string(sub_grid)
				new_sub_grid = string_to_array(rules[sub_grid])
				for k in range(3):
					for l in range(3):
						if (3*i+k) not in new_grid:
							new_grid[3*i+k]={}
						new_grid[3*i+k][3*j+l] = new_sub_grid[k][l] 


	else:
		for i in range(len(grid[0])/3):
			for j in range(len(grid[0])/3):
				# print i,j,grid
				sub_grid = []
				for ii in range(3):
					sgr = []
					for jj in range(3):
						sgr.append(grid[3*i+ii][3*j+jj])
					sub_grid.append(sgr)
				# sub_grid = grid[3*i:3*i+3][3*j:3*j+3]
				sub_grid = array_to_string(sub_grid)
				new_sub_grid = string_to_array(rules[sub_grid])
				for k in range(4):
					for l in range(4):
						if (4*i+k) not in new_grid:
							new_grid[4*i+k]={}
						new_grid[4*i+k][4*j+l] = new_sub_grid[k][l] 

	grid = new_grid

cnt = 0
for row in grid.values():
	print row
	for val in row.values():
		if val == '#':
			cnt += 1
print cnt

sys.exit()