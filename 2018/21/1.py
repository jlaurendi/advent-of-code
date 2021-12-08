import sys, copy


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

# ip = 0
# regs = [0] * 6
# regs[0]=0
# ticks = 0
# first_r3 = None
# prev_r3 = None
# while True:
# 	# print ip, ticks, regs

# 	if ip > len(instructions)-1:
# 		print "BROKE in : "+ str(ticks)
# 		break
# 	ins = instructions[ip]
# 	op = ins[0]
# 	a = int(ins[1])
# 	b = int(ins[2])
# 	c = int(ins[3])

# 	if ip == 29:
# 		if first_r3 == None:
# 			first_r3 = regs[3]
# 		else:
# 			if regs[3] == first_r3:
# 				print prev_r3
# 				sys.exit()
# 			else:
# 				prev_r3 = regs[3]


# 		# if regs[3] in r3_vals:
# 			# sys.exit()

# 		# r3_vals.append(regs[3])
# 		# print bin(regs[3])
# 		# print ins, op, a, b, c, regs, ticks
# 		# sys.exit()
# 	regs[ip_reg] = ip
# 	regs = perform_op(op, a, b, c, regs)
# 	ip = regs[ip_reg]
# 	ip += 1
# 	ticks +=1
# 	# if ticks > 1000:
# 	# 	break


def hand_compiled():
	r3 = 0
	r0 = 0
	first_r3 = None
	while True:
		r2 = r3 | 0b10000000000000000
		r3 = 1505483
		while True:
			break2 = False
			r4 = r2 & 0b11111111
			r3 += r4
			r3 &= 0b111111111111111111111111
			r3 *= 65899
			r3 &= 0b111111111111111111111111
			if r2 <= 256:
				r4 = 0
				while True:
					r5 = (r4 + 1) * 256
					if r5 >= r2:
						r2 = r4
						break2 = True
						break
					r4 += 1
			else:
				break
			if break2:
				break

		if first_r3 == None:
			first_r3 = r3
			print r3
			sys.exit()
		else:
			if r3 == first_r3:
				print prev_r3
				sys.exit()
			else:
				prev_r3 = r3
		if r3 == r0:
			break

hand_compiled()

# 9638656