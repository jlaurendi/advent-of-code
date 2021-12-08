import sys,math,copy
with open('advent-input.txt') as f:
#with open('advent-test.txt') as f:
    a = f.readlines()

tape = {}
cursor = 0
cur_state = 'A'

for i in xrange(12317297):

	if cursor not in tape:
		tape[cursor] = 0

	cur_val = tape[cursor]
	if cur_state == 'A':
		if cur_val == 0:
			tape[cursor] = 1
			cursor += 1
			cur_state = 'B'
		else:
			tape[cursor] = 0
			cursor -= 1
			cur_state = 'D'
	elif cur_state == 'B':
		if cur_val == 0:
			tape[cursor] = 1
			cursor += 1
			cur_state = 'C'
		else:
			tape[cursor] = 0
			cursor += 1
			cur_state = 'F'
	elif cur_state == 'C':
		if cur_val == 0:
			tape[cursor] = 1
			cursor -= 1
			cur_state = 'C'
		else:
			tape[cursor] = 1
			cursor -= 1
			cur_state = 'A'
	elif cur_state == 'D':
		if cur_val == 0:
			tape[cursor] = 0
			cursor -= 1
			cur_state = 'E'
		else:
			tape[cursor] = 1
			cursor += 1
			cur_state = 'A'
	elif cur_state == 'E':
		if cur_val == 0:
			tape[cursor] = 1
			cursor -= 1
			cur_state = 'A'
		else:
			tape[cursor] = 0
			cursor += 1
			cur_state = 'B'
	elif cur_state == 'F':
		if cur_val == 0:
			tape[cursor] = 0
			cursor += 1
			cur_state = 'C'
		else:
			tape[cursor] = 0
			cursor += 1
			cur_state = 'E'
	else:
		print 'trouble'
		sys.exit()

csum = 0
for i in tape:
	if tape[i] == 1:
		csum += 1

print csum

sys.exit()
