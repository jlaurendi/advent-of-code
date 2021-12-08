import sys
with open('advent-input.txt') as f:
    a = f.readlines()

graph = {}
for l in a:
	parts = l.split(" <-> ")
	idx = int(parts[0])	
	cxns = parts[1].strip().split(",")
	graph[idx] = []
	for c in cxns:
		graph[idx].append(int(c.strip()))

groups = []
for g in graph:
	already_seen = False
	for grp in groups:
		if g in grp:
			already_seen = True
			break

	if already_seen:
		continue		

	nodes_seen = {}
	nodes_to_explore = [g]

	while True:
			old_count = len(nodes_seen)
			next_nodes = []
			for n in nodes_to_explore:
				nodes_seen[n] = True
				for nn in graph[n]:
					if nn not in nodes_seen:
						next_nodes.append(nn)

			print old_count

			if len(nodes_seen) == old_count:
				groups.append(nodes_seen)
				break

			nodes_to_explore = next_nodes

print groups
print len(groups)