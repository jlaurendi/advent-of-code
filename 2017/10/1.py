import sys
with open('advent-input.txt') as f:
    a = f.readlines()
    a = [int(i) for i in a[0].split(',')]

n = 256
lst = range(n)
pos = 0
skip = 0
for l in a:

	for i in range(l/2):
		idx1 = (pos + i) % n
		idx2 = (pos + l - i - 1) % n
		tmp = lst[idx1]
		lst[idx1] = lst[idx2]
		lst[idx2] = tmp

	pos = (pos + l + skip) % n

	skip += 1

print lst[0]*lst[1]