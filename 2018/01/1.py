import sys
with open('advent-input.txt') as f:
    a = f.readlines()

seen = {}
seen[0] = 1
tot = 0
while True:
	for l in a:
		tot += int(l)
		if tot in seen:
			print(tot)
			sys.exit()
		else:
			seen[tot] = 1

print 'none'
