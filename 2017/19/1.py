import sys
with open('advent-input.txt') as f:
    a = f.readlines()

grid = {}
i = 0
num_rows = 0
num_cols = 0
all_ltrs = set()
for ln in a:
	j = 0
	grid[i] = {}
	for char in ln.strip("\n"):
		grid[i][j] = char

		if char.isalpha():
			all_ltrs.add(char)

		if i > num_rows:
			num_rows = i

		if j > num_cols:
			num_cols = j

		j += 1
	i += 1

x = None
y = 0
for pos in grid[0]:
	char = grid[0][pos]
	if char == '|':
		x = pos

d = 'd'
ltrs = ''
ltrs_seen = set()
steps = 0
while True:

	char = grid[y][x]
	print x,y,char

	if char.isalpha():
		print char
		ltrs += char
		ltrs_seen.add(char)
	elif char == '+':
		if d == 'u' or d == 'd':
			if grid[y][x+1] == '-' or grid[y][x+1].isalpha():
				d = 'r'
			elif grid[y][x-1] == '-' or grid[y][x-1].isalpha():
				d = 'l'
		else:
			if grid[y+1][x] == '|' or grid[y+1][x].isalpha():
				d = 'd'
			elif grid[y-1][x] == '|' or grid[y-1][x].isalpha():
				d = 'u'
			else:
				print 'PROBLEM'
				sys.exit()

	if d == 'd':
		y += 1
	elif d == 'u':
		y -= 1
	elif d == 'r':
		x += 1
	elif d == 'l':
		x -= 1


	steps += 1
	if all_ltrs == ltrs_seen:
		break

		# if char == '-':
		# 	grid[i][j] = '-'
		# elif char == '+':

		# elif char == '|':

		# elif char.isalpha():

		# else:
print steps