import sys, copy
ip_reg = 0
instructions = []
with open('advent-input.txt') as f:
	a = f.readlines()

	for line in a:
		if line[0] == '#':
			line = line.split('#ip ')
			ip_reg = int(line[1])
		else:
			line = line.strip().split(' ')
			instructions.append(line)

def perform_op(op_num, a, b, c, regs):
	if op_num == 'addr': # addr
		regs[c] = regs[a]+regs[b]
	elif op_num == 'addi': # addi
		regs[c] = regs[a]+b
	elif op_num == 'mulr': #mulr
		regs[c] = regs[a]*regs[b]
	elif op_num == 'muli': #muli
		regs[c] = regs[a]*b
	elif op_num == 'banr': #banr
		regs[c] = regs[a]&regs[b]
	elif op_num == 'bani': #bani
		regs[c] = regs[a]&b
	elif op_num == 'borr':
		regs[c] = regs[a]|regs[b]
	elif op_num == 'bori':
		regs[c] = regs[a]|b
	elif op_num == 'setr':
		regs[c] = regs[a]
	elif op_num == 'seti':
		regs[c] = a
	elif op_num == 'gtir':
		regs[c] = 1 if a > regs[b] else 0
	elif op_num == 'gtri':
		regs[c] = 1 if regs[a] > b else 0
	elif op_num == 'gtrr':
		regs[c] = 1 if regs[a] > regs[b] else 0
	elif op_num == 'eqir':
		regs[c] = 1 if a == regs[b] else 0
	elif op_num == 'eqri':
		regs[c] = 1 if regs[a] == b else 0
	elif op_num == 'eqrr':
		regs[c] = 1 if regs[a] == regs[b] else 0
	else:
		print "Unknown: "+op_num

	return regs

ip = 0
regs = [0] * 6
regs[0]=1
ticks = 0
while True:
	# print ip, regs

	if ip > len(instructions)-1:
		break
	ins = instructions[ip]
	op = ins[0]
	a = int(ins[1])
	b = int(ins[2])
	c = int(ins[3])

	regs[ip_reg] = ip
	regs = perform_op(op, a, b, c, regs)
	ip = regs[ip_reg]
	ip += 1
	ticks +=1
	if ip == 11:
		print regs
	if ticks > 1000:
		break

print regs[0]

# 7649054
# 25849500
# 18200448
# 7649053
# 7649055
