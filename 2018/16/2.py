import sys, copy

samples = []
with open('advent-input.txt') as f:
	a = f.readlines()

	for i in xrange(len(a)):
		line = a[i]
		if "Before" in line:
			regs_before = line.strip().split('Before: ')[1].strip('[').strip(']').split(',')
			regs_before = [int(j) for j in regs_before]

			inst = a[i+1].strip().split(' ')
			inst = [int(j) for j in inst]

			line = a[i+2]

			regs_after = line.strip().split('After:')[1].strip().strip('[').strip(']').split(',')
			regs_after = [int(j) for j in regs_after]

			samples.append([regs_before, inst, regs_after])

def perform_op(op_num, a, b, c, regs):
	if op_num == 0: # addr
		regs[c] = regs[a]+regs[b]
	elif op_num == 1: # addi
		regs[c] = regs[a]+b
	elif op_num == 2: #mulr
		# print a,b,c
		# print regs[a],regs[b],regs[c]
		regs[c] = regs[a]*regs[b]
	elif op_num == 3: #muli
		regs[c] = regs[a]*b
	elif op_num == 4: #banr
		regs[c] = regs[a]&regs[b]
	elif op_num == 5: #bani
		regs[c] = regs[a]&b
	elif op_num == 6:
		regs[c] = regs[a]|regs[b]
	elif op_num == 7:
		regs[c] = regs[a]|b
	elif op_num == 8:
		regs[c] = regs[a]
	elif op_num == 9:
		regs[c] = a
	elif op_num == 10:
		regs[c] = 1 if a > regs[b] else 0
	elif op_num == 11:
		regs[c] = 1 if regs[a] > b else 0
	elif op_num == 12:
		regs[c] = 1 if regs[a] > regs[b] else 0
	elif op_num == 13:
		regs[c] = 1 if a == regs[b] else 0
	elif op_num == 14:
		regs[c] = 1 if regs[a] == b else 0
	elif op_num == 15:
		regs[c] = 1 if regs[a] == regs[b] else 0

	return regs

regs = [0] * 4
total_cnt = 0

op_options = {}
for i in range(16):
	op_options[i] = []
	for j in range(16):
		op_options[i].append(j)

for s in samples:
	inst = s[1]

	regs_before = s[0]
	regs_after = s[2]
	cnt = 0
	# print inst, regs_before, regs_after
	working_op = None
	for i in range(16):
		op_output = perform_op(i, inst[1], inst[2], inst[3], regs_before[:])
		if op_output != regs_after:
			if i in op_options[inst[0]]:
				op_options[inst[0]].remove(i)
			# working_op = i
			# cnt += 1
			# if cnt >= 3:
			# 	total_cnt += 1
			# 	break

	if cnt == 1:
		print str(inst[0])+" = "+str(working_op)

while True:
	nxt = None
	for i in op_options:
		if type(op_options[i]) is list and len(op_options[i]) == 1:
			nxt = op_options[i][0]
			op_options[i] = op_options[i][0]
			break

	for j in op_options:
		if type(op_options[j]) is list and nxt in op_options[j]:
			op_options[j].remove(nxt)

	if nxt == None:
		break

# print op_options

instructions = []
with open('advent-input3.txt') as f:
	a = f.readlines()

	for i in a:
		inst = i.strip().split()
		inst = [int(j) for j in inst]

		instructions.append(inst)

regs = [0] * 4
for ins in instructions:
	op_num = op_options[ins[0]]
	regs = perform_op(op_num, ins[1], ins[2], ins[3], regs)

print regs[0]