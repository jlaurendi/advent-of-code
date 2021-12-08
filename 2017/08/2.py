import sys
ans = 0
with open('input.txt') as f:
    a = f.readlines()
    a = [line.strip() for line in a]

def cond_met(regs, cond_reg, cond_op, cond_amt):
	if cond_op == '<':
		return regs[cond_reg] < cond_amt
	elif cond_op == '<=':
		return regs[cond_reg] <= cond_amt
	elif cond_op == '!=':
		return regs[cond_reg] != cond_amt
	elif cond_op == '>':
		return regs[cond_reg] > cond_amt
	elif cond_op == '>=':
		return regs[cond_reg] >= cond_amt
	elif cond_op == '==':
		return regs[cond_reg] == cond_amt
	else:
		print "UNKNOWN OP"
		print cond_op
		sys.exit()

regs = {}
max_seen = 0
for i, l in enumerate(a):
	parts = l.split()
	reg = parts[0]
	op = parts[1]
	amt = int(parts[2])
	cond_reg = parts[4]
	cond_op = parts[5]
	cond_amt = int(parts[6])

	if reg not in regs:
		regs[reg] = 0

	if cond_reg not in regs:
		regs[cond_reg] = 0

	if cond_met(regs, cond_reg, cond_op, cond_amt):
		if op == 'inc':
			regs[reg] += amt
		elif op == 'dec':
			regs[reg] -= amt

	curr_max = int(regs[max(regs, key=regs.get)])
	if curr_max > max_seen:
		max_seen = curr_max
		print max_seen

#print regs
#print max(regs, key=regs.get)
#print regs[max(regs, key=regs.get)]
print max_seen
