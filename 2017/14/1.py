import sys


def knot_hash(a):
	a = [ord(i) for i in a]
	a = a + [17, 31, 73, 47, 23]

	n = 256
	lst = range(n)
	pos = 0
	skip = 0
	for rnd in range(64):
		for l in a:

			for i in range(l/2):
				idx1 = (pos + i) % n
				idx2 = (pos + l - i - 1) % n
				tmp = lst[idx1]
				lst[idx1] = lst[idx2]
				lst[idx2] = tmp

			pos = (pos + l + skip) % n

			skip += 1

	dense = []
	for i in range(n/16):
		res = 0
		for j in range(16):
			res ^= lst[16*i+j]
		dense.append(res)

	knot = ""
	for c in dense:
		knot += hex(c)[2:]

	return knot

ipt = "stpzcrnm"
num_open = 0
for i in range(128):
	s = ipt + "-"+str(i)
	hsh = knot_hash(s)
	for char in hsh:
		char = int(char, 16)
		for j in range(4):
			if char % 2 != 0:
				num_open += 1
			char = char / 2

print num_open
sys.exit()