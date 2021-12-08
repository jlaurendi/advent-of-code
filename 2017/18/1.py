import sys
with open('advent-input.txt') as f:
    a = f.readlines()

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

instrs = []
regs = {}
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
	regs[reg] = 0

print instrs

ptr = 0
sounds = []
while True:
	full_ins = instrs[ptr]

	ins = full_ins[0]
	if ins == "snd":
		val = full_ins[1]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		sounds.append(val)
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
		if regs[full_ins[1]] != 0:
			print sounds[-1]
			sys.exit()
	elif ins == "jgz":
		val = full_ins[2]
		if check_int(val):
			val = int(val)
		else:
			val = regs[val]

		if regs[full_ins[1]] > 0:
			ptr += val
			continue
	else:
		print "ERROR"
		sys.exit()

	ptr += 1
