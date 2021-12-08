import sys, copy

nodes = []
with open('advent-input.txt') as f:
	a = f.readlines()

	for i in a:
		n = [int(j) for j in i.strip().split(',')]
		nodes.append(n)

constellations = []

for n in nodes:
	constellations.append([n])

def dist(n1, n2):
	d = 0
	for i in xrange(len(n1)):
		d += abs(n1[i] - n2[i])
	return d

while True:
	# print constellations
	new_constellations = []
	merged = False
	change_made = False
	merged_node = None
	for c1 in constellations:
		if merged:
			if c1 != merged_node:
				new_constellations.append(c1)
		else:
			for n1 in c1:
				for c2 in constellations:
					if c1 == c2:
						continue
					for n2 in c2:
						d = dist(n1, n2)
						if d <= 3:
							new_constellations.append(c1+c2)
							change_made = True
							merged = True
							merged_node = c2
							break
					if merged:
						break
				if merged:
					break

			if not merged:
				new_constellations.append(c1)

		# if merged:
		# 	break

	constellations = copy.deepcopy(new_constellations)
	# for c in constellations:
	# 	print c
	# sys.exit()

	if not change_made:
		break


print len(constellations)
