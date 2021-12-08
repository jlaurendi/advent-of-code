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
	max_depth = max(wall.keys())
	sev = 0
	psns = orig_psns

	for i in range(delay):
		for p in psns:
			mod = (wall[p]-1)*2
			psns[p] = (psns[p] + 1) % mod

	caught = False
	for i in range(max_depth+1):

		if i in wall and psns[i] == 0:
			sev += wall[i] * i
			caught = True
			break

		for p in psns:
			mod = (wall[p]-1)*2
			psns[p] = (psns[p] + 1) % mod

	if not caught:
		print delay
		sys.exit()
		
	delay += 1

print psns
print sev