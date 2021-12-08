import sys,math,copy
with open('advent-input.txt') as f:
#with open('advent-test.txt') as f:
    a = f.readlines()

grid = {}
i = 0
for ln in a:
	row = {}
	ln = ln.strip("\n")
	j = 0
	for c in ln:
		row[j] = c
		j+=1

	grid[i] = row
	i+=1

num_infxns = 0

d = 'u'
cur_x = len(grid[0])/2
cur_y = len(grid[0])/2
print cur_x,cur_y
for i in xrange(10000):
	if cur_x not in grid:
		grid[cur_x] = {}
	if cur_y not in grid[cur_x]:
		grid[cur_x][cur_y] = '.'
	# update d
	if grid[cur_x][cur_y] == '#':
		if d == 'u': 
			d = 'r'
		elif d == 'r': 
			d = 'd'
		elif d == 'd':
			d = 'l'
		elif d == 'l':
			d = 'u'

	else:
		if d == 'u': 
			d = 'l'
		elif d == 'l': 
			d = 'd'
		elif d == 'd':
			d = 'r'
		elif d == 'r':
			d = 'u'

	if grid[cur_x][cur_y] == '.':
		grid[cur_x][cur_y] = '#'
		num_infxns += 1
	else:
		grid[cur_x][cur_y] = '.'

	if d == 'u': 
		cur_x -= 1
	elif d == 'l': 
		cur_y -= 1
	elif d == 'd':
		cur_x += 1
	elif d == 'r':
		cur_y += 1


print num_infxns
sys.exit()