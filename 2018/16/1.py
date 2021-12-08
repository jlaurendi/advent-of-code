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
		print a,b,c
		print regs[a],regs[b],regs[c]
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
for s in samples:
	inst = s[1]

	regs_before = s[0]
	regs_after = s[2]
	cnt = 0
	print inst, regs_before, regs_after
	for i in range(16):
		op_output = perform_op(i, inst[1], inst[2], inst[3], regs_before[:])
		print op_output
		if op_output == regs_after:
			cnt += 1
			if cnt >= 3:
				total_cnt += 1
				break

print total_cnt