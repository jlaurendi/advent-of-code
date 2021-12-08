import sys
with open('advent-input.txt') as f:
    a = f.readlines()
    a = [ord(i) for i in a[0]] + [17, 31, 73, 47, 23]

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

final = ""
for c in dense:
	final += hex(c)[2:]
print final
