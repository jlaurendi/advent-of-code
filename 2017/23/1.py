import sys,math,copy
with open('advent-input.txt') as f:
#with open('advent-test.txt') as f:
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
		if reg == 'a':
			all_regs[reg] = 1
		else:
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

num_mul = 0
old_h = None
def run_step(p):
	global num_1_sent
	global num_mul
	global old_h
	ptr = ptrs[p]
	regs = all_regs[p]
	msgs_recv = msgs[p]
	msgs_send = msgs[(p+1)%len(msgs)]


	try:
		full_ins = instrs[ptr]
		ins = full_ins[0]

		print full_ins
		if regs['h'] != old_h:
			print old_h
			old_h = regs['h']
	except:
		print regs['h']
		sys.exit()

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
	elif ins == "sub":
		val = full_ins[2]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		regs[full_ins[1]] -= int(val)

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
		num_mul += 1
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
	elif ins == "jnz":
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

		if val1 != 0:
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

	run_step(0)



print num_mul