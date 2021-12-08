import sys
with open('advent-input.txt') as f:
    a = f.readlines()

wall = {}
orig_psns = {}
for ln in a:
	b = ln.split(": ")
	depth = int(b[0].strip())
	rng = int(b[1].strip())
	wall[depth] = rng
	orig_psns[depth] = 0


delay = 0
while True:

	caught = False
	for w in wall:
		mod = (wall[w]-1)*2
		if (delay + w) % mod == 0:
			caught = True
			break

	if not caught:
		print delay
		sys.exit()

	delay += 1
