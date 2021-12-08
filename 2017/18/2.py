import sys, copy
with open('advent-input.txt') as f:
    a = f.readlines()

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

instrs = []
all_regs = {}
for aa in a:
	num = None

	if len(aa.split(" ")) == 2:
		instr, reg = aa.split(" ")
	else:
		instr, reg, num = aa.split(" ")

	reg = reg.strip()
	if num:
		num = num.strip()

	instrs.append([instr, reg, num])

	if not check_int(reg):
		all_regs[reg] = 0

num_1_sent = 0
sounds = []
ptrs = [0, 0]
states = [0, 0]
regs_a = copy.deepcopy(all_regs)
regs_b = copy.deepcopy(all_regs)
all_regs = [regs_a, regs_b]
msgs = [[], []]

all_regs[0]['p'] = 0
all_regs[1]['p'] = 1

def run_step(p):
	global num_1_sent
	ptr = ptrs[p]
	regs = all_regs[p]
	msgs_recv = msgs[p]
	msgs_send = msgs[(p+1)%len(msgs)]

	full_ins = instrs[ptr]
	ins = full_ins[0]

	if ins == "snd":
		val = full_ins[1]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		msgs_send.append(val)
		if p == 1:
			num_1_sent += 1
	elif ins == "set":

		val = full_ins[2]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		regs[full_ins[1]] = int(val)
	elif ins == "add":
		val = full_ins[2]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		regs[full_ins[1]] += int(val)
	elif ins == "mul":
		val = full_ins[2]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		regs[full_ins[1]] *= int(val)
	elif ins == "mod":
		val = full_ins[2]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		regs[full_ins[1]] %= int(val)
	elif ins == "rcv":
		if len(msgs_recv) == 0:
			states[p] = 1
			return
		else:
			val = msgs_recv.pop(0)

		regs[full_ins[1]] = val

	elif ins == "jgz":
		val = full_ins[2]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		val1 = full_ins[1]
		if check_int(val1):
			val1 = int(val1)
		else:
			val1 = regs[val1]

		if val1 > 0:
			ptr += val
			if ptr >= len(instrs) or ptr < 0:
				states[p] = 2

			ptrs[p] = ptr
			return
	else:
		print "ERROR"
		sys.exit()

	ptr += 1
	if ptr >= len(instrs) or ptr < 0:
		states[p] = 2

	ptrs[p] = ptr

step = 0
while True:

	if states[0] != 2:
		run_step(0)

	if states[1] != 2:
		run_step(1)

	# print ptrs
	# print states
	# print msgs
	# print all_regs
	# if step > 10:
	# 	sys.exit()
	# step +=1


	if (states[0] == 1 and states[1] == 1) or (states[0] == 2 and states[1] == 2):
		break

print num_1_sent